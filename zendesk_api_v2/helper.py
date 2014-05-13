
class APIHelperException(Exception):
	pass

class Helper(object):
	
	def __init__(self, cls, items=[],
				next_page=None, 
				prev_page=None,
				sideloaded_results={},
				method='fetch'):

		self.cls = cls
		self.items = items
		self.next_page = next_page
		self.prev_page = prev_page
		self.method = method
		self.sideloaded_results = sideloaded_results

	def get_sideloaded(self):

		return self.sideloaded_results

	def has_next(self):
		
		return True if self.next_page is not None else False

	def has_prev(self):
		
		return True if self.prev_page is not None else False

	def next(self, api):
		
		if self.method == 'fetch':
			#print self.next_page
			result = self.cls.fetch(api,
				url=self.next_page)
		
		elif self.method == 'query':
			
			result = self.cls.query(api,
				url=self.next_page)
		
		else:
			raise APIHelperException('reason: method not found')
		
		return result

	def prev(self, api):
		if self.method == 'fetch':
			
			result = self.cls.fetch(api,
				url=self.prev_page)
		
		elif self.method == 'query':
			
			result = self.cls.query(api,
				url=self.prev_page)
		
		else:
			raise APIHelperException('reason: method not found')
		
		return result
	
	def all(self):

		return self.items

	def count(self):

		return len(self.items)
