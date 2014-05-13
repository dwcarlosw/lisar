import requests
import inspect
import urlparse

try:
	import ujson as json
except:
	import json

from helper import Helper

ZENDESK_API_VERSION = 2
PER_PAGE = 100

class ZendeskAPIException(Exception):
	pass

class ZendeskAPIValidationException(ZendeskAPIException):
	pass

class ZendeskAPI(object):

	def __init__(self, *args, **kwargs):

		self.user = kwargs.get('user')
		self.password = kwargs.get('password')
		self.url = kwargs.get('url')

	def _get_cls_model(self, obj):
		
		if inspect.isclass(obj):
			model = obj.__name__.lower()
			cls = obj
		else:
			model = obj.__class__.__name__.lower()
			cls = obj.__class__
		return (cls, model)

	def _get_query(self, obj, query):

		cls, model = self._get_cls_model(obj)
		
		q = '?query=type:%s' % (model)
		return q  + self._get_search_query(query)

	def _get_search_query(self, query):

		q = ''
		for qry in query:
			p = qry[0]
			o = qry[1]
			v = qry[2]
			if o == '=':
				q += ' %s%s%s' % (p, ':', v)
			elif o == '<':
				q += ' %s%s%s' % (p, '<', v)
			elif o == '>':
				q += ' %s%s%s' % (p, '>', v)
			elif o == 'like':
				q += ' %s%s%s' % (p, ':', v + '*')
		return q

	def _get_url_per_page(self, url):
		per_page = 'per_page=%s' % (PER_PAGE)
		
		if urlparse.urlparse(url)[4]:
			url += '&' + per_page
		else:
			url += '?' + per_page
		return url

	def _get_execute(self, *args, **kwargs):
		try:
			headers = {'Accept':'application/json'}
			url = kwargs.get('url')
			
			if not url.startswith('http'):
				url = '%s/api/v%s/%s' % (self.url, 
									ZENDESK_API_VERSION, 
									url
									)
				url = self._get_url_per_page(url)
			
			response = requests.get(url, 
								auth=(self.user, self.password),
								headers=headers
								)

			return response.json()

		except Exception as e:
			raise ZendeskAPIException('reason: %s' % (e))


	def _upload_execute(self, *args, **kwargs):

		try:
			mimetype = kwargs.get('mimetype')
			headers = {'Content-Type':mimetype}

			data = kwargs.get('item_data', None)

			url = '%s/api/v%s/%s' % (self.url, 
								ZENDESK_API_VERSION, 
								kwargs.get('url')
								)

			response = requests.post(url, 
							data=data, auth=(self.user, self.password),
							headers=headers
							)
			
			json = response.json()

			self._validate(json)

			return json

		except Exception as e:
			raise ZendeskAPIException('reason: %s' % (e))


	def _put_execute(self, *args, **kwargs):

		try:

			headers = {'Accept':'application/json', 'Content-Type':'application/json'}
			data = kwargs.get('item_data', {})
			sub_method = kwargs.get('sub_method')
			url = '%s/api/v%s/%s' % (self.url, 
								ZENDESK_API_VERSION, 
								kwargs.get('url')
								)

			if sub_method == 'update':
				response = requests.put(url, auth=(self.user, self.password),
										data=json.dumps(data),
										headers=headers)
			else:
				response = requests.post(url, auth=(self.user, self.password),
											data=json.dumps(data),
											headers=headers)
			return response.json()

		except Exception as e:
			raise ZendeskAPIException('reason: %s' % (e))

	def _delete_execute(self, *args, **kwargs):

		try:

			url = '%s/api/v%s/%s' % (self.url, 
								ZENDESK_API_VERSION, 
								kwargs.get('url')
								)
			
			response = requests.delete(url, auth=(self.user, self.password))

			if not response.status_code == requests.codes.ok:
				return response.text
			
			return 'success'

		except Exception as e:
			raise ZendeskAPIException('reason: %s' % (e))

	def _delete_parsed(self, *args, **kwargs):
		
		response = kwargs.get('data')

		if response != 'success':
			self._validate(json.loads(response))

	def _put_parsed(self, *args, **kwargs):
		
		response = kwargs.get('data')
		obj = kwargs.get('obj')
		
		override = kwargs.get('override', None)
		model = kwargs.get('model')
		if override is not None:
			model = override
		
		self._validate(response)

		kwargs = response.get(model, None)
		if kwargs is not None:
			obj.update(**kwargs)

		return obj

	def _validate(self, data):

		details = data.get('details',None)
		# description = data.get('description', None)
		error = data.get('error', None)

		if details is not None:
			parse = ''
			for key, val in details.iteritems():
				parse += key + ': '
				for d in val:
					parse += d['description'] +' '
				parse += '     '
			#raise ZendeskAPIValidationException(data)
			raise ZendeskAPIValidationException('%s' % parse)

		# elif description is not None:
		# 	raise ZendeskAPIValidationException('Error: %s' % description)

		elif error is not None:
			if ('title' in error) and ('message' in error):
				raise ZendeskAPIValidationException(error['title'] + ': ' + error['message'])
			else:
				raise ZendeskAPIValidationException(error)

		# elif error is not None:
		# 	raise ZendeskAPIValidationException('Error: %s' % data)

	def _get_url_param(self, url, param):

		parsed = urlparse.urlparse(url)
		data = urlparse.parse_qs(parsed.query)

		return data.get(param, [])

	def _get_parsed(self, *args, **kwargs):

		url = kwargs.get('url')
		#print url

		includes = self._get_url_param(url, 'include')

		obj = kwargs.get('obj')
		cls, model = self._get_cls_model(obj)

		response = kwargs.get('data')

		self._validate(response)

		override = kwargs.get('override', None)

		if override is None:
			data = response.get('%s' % (model), None)
			if data is None:
				data = response.get('%ss' % (model), None)
		else:
			data = response.get('%s' % (override), None)

		sideloaded_results = {}
		if includes:
			"""
			This handles any side-loaded results
			"""
			for include in includes:
				sideloaded_results[include] = response.get(include, [])
		
		if data is None:
			raise ZendeskAPIException

		if isinstance(data, list):
			items = []
			
			method = kwargs.get('method')
			
			next_page = response.get('next_page', None)
			prev_page = response.get('prev_page', None)
			#print 'next page' + str(next_page)
			#print 'prev_page' + str(prev_page)

			for kwargs in data:
				items.append(cls(**kwargs))
			
			helper = Helper(cls, items=items, next_page=next_page,
								prev_page=prev_page, method=method,
								sideloaded_results=sideloaded_results
							)
			
			return helper

		elif isinstance(data, dict):

			return cls(**data)

		return None

	def _get_object_by_id(self, items, id):

		for item in items:
			if item.id == id:
				return item
		return None

'''
TESTS:
------

from tickets import Ticket, Audit, Comment, Ticket_Metric, Ticket_Form, Ticket_Field
from users import User, Group, Group_Membership, User_Field, Custom_Role, Identitie
from views import View
from attachments import Attachment, Upload
from organizations import Organization,Organization_Field

api = ZendeskAPI(user='oleg.p@broadconnect.ca', 
					password='Kop721suk', 
					url='https://broadconnectusa.zendesk.com'
				)

files =[{'file':open('test2.png', 'rb'), 'name':'test2.png', 'mimetype':'image/png'}]

tokens, attachments = Upload.upload(api, files=files)
'''

'''

curl tests:

curl -v -u oleg.p@broadconnect.ca:Kop721suk -H 'Content-Type: image/jpeg' --data-binary @test3.jpeg -X POST 'https://broadconnectusa.zendesk.com/api/v2/uploads.json?filename="test.jpeg"


urrlib2 tests:

import urllib2
#from urlparse import urlparse, urlunparse
#from ntlm import HTTPNtlmAuthHandler
import base64
import os
image_path = 'test2.png'
url = 'https://broadconnectusa.zendesk.com/api/v2/uploads.json?filename=test2.png'
base64string = base64.encodestring('%s:%s' % ('oleg.p@broadconnect.ca', 'Kop721suk'))[:-1]
authheader =  "Basic %s" % base64string
length = os.path.getsize(image_path)
png_data = open(image_path, "rb")
print length
request = urllib2.Request(url, data=png_data)
request.add_header("Authorization", authheader)
request.add_header('Cache-Control', 'no-cache')
request.add_header('Content-Length', '%d' % length)
#request.add_header('Content-Length', 'NULL')
request.add_header('Content-Type', 'image/png')
res = urllib2.urlopen(request).read().strip()

r = json.loads(res)

#open('pdf-test.pdf', 'r')
#request.FILES['myfile'].read()

files = {'file':open('pdf-test.pdf', 'rb')}
headers = {'Content-Type':'application/binary'}

r = requests.post('https://broadconnectusa.zendesk.com/api/v2/uploads.json?filename=test.pdf', 
				files=files, auth=('oleg.p@broadconnect.ca', 'Kop721suk'),
				headers=headers
				)

print r.json()
'''
'''
{"ticket":{"subject":"Testing ticket with attachment","description":"Please take a look at this file","uploads":"108428706"}}"

{"ticket":{"subject":"Testing ticket with attachment","description":"Please take a look at this file","uploads":{attachments:["108428706"]}}}"

{"ticket":{"subject":"Testing ticket with attachment","description":"Please take a look at this file","attachments":["108428706"]}}"
'''

'''

#request.FILES['docfile']
#data = request.FILES['myfile'].read()

file = request.FILES['filename']
file.name           # Gives name
file.content_type   # Gives Content type text/html etc
file.size           # Gives file's size in byte
file.read()         # Reads file

#"https://helpdesk.zendesk.com/api/v2/uploads.json?filename=myfile.dat&token={optional_token}"

files = {'file':open('pdf-test.pdf', 'r')}
#print files

headers = {'Accept':'application/json', 'Content-Type':'application/binary'}

r = requests.post('https://broadconnectusa.zendesk.com/api/v2/uploads.json?filename=test.pdf', 
				files=files, auth=('oleg.p@broadconnect.ca', 'Kop721suk'),
				headers=headers
				)
print r.json()

#r = requests.get('https://broadconnectusa.zendesk.com/api/v2/attachments/349056444.json', 
#				auth=('oleg.p@broadconnect.ca', 'Kop721suk')
#				)

#print r.json()

#u = Upload()
'''


