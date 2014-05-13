from base import Model
import inspect
from endpoints import MAPPED_URLS

class Upload(object):

	@classmethod
	def upload(cls, api, *args, **kwargs):
		"""
		- Handles upload of multiple files
		- returns results as a collection of attachments

		TODO: integrate better with api wrapper
		since upload have a unique request and response
		"""
		method = inspect.stack()[0][3]
		model = cls.__name__.lower()
		files = kwargs.get('files', [])
		data = {}
		token = None
		tokens = []
		for item in files:
			open_file = item.get('file', None)
			filename = item.get('name', 'file')
			mimetype = item.get('mimetype', None)
			url = MAPPED_URLS.get(model).get(method)
			url = url.format(**{'filename':filename, 'model':model})
			if token is not None:
				url += '&token=%s' % (token)
			json = api._upload_execute(item_data=open_file, url=url, mimetype=mimetype)
			data = json.get(model)
			token = data.get('token')
			tokens.append(token)

		"""
		At the final call response attachments will be populated with all the uploaded
		files (ie: in case of multiple attachments)
		"""
		attachments = data.get('attachments', [])
		items = []
		for item in attachments:
			items.append(Attachment(**item))
		return (tokens, items)

class Attachment(Model):
	pass