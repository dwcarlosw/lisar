
import inspect
from endpoints import MAPPED_URLS

class Base(object):

	def __init__(self, **kwargs):

		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __getattr__(self, name):

		return None
	
	def update(self, **kwargs):

		for k, v in kwargs.iteritems():
			setattr(self, k, v)

class ModelException(Exception):
	pass

class ModelEndpointException(ModelException):
	pass

class Model(Base):

	def _override_relation(self, **kwargs):

		kwargs.update({
			'override_relation':self.__class__.__name__.lower()
			})
		return kwargs

	@classmethod
	def _get_object_by_id(cls, items, id):

		for item in items:
			if item.id == id:
				return item
		return None

	@classmethod
	def _get_mapped_url(cls, model, method, override_relation):

		data = MAPPED_URLS.get(model)
		data = data.get(method)

		if isinstance(data, dict):
			data = data.get(override_relation)

		return data

	def _put_mapped_url(self, model, method, sub_method):

		data = MAPPED_URLS.get(model)
		data = data.get(method)
		return data.get(sub_method)

	def _delete_mapped_url(self, model, method):

		data = MAPPED_URLS.get(model)
		return data.get(method)

	@classmethod
	def _get_model_execute(cls, api, *args, **kwargs):
		url = kwargs.get('url')
		#print url
		data = api._get_execute(url=url)

		return api._get_parsed(data=data, obj=cls, 
					override=kwargs.get('override', None),
					method=kwargs.get('method', None), 
					url=url
					)
	
	@classmethod
	def query(cls, api, query=[], sort_by=None, sort_order=None, url=None):

		if url is None:
			url = 'search.json' + api._get_query(cls, query)
			if sort_by is not None:
				url += '&sort_by=%s' % (sort_by)
			if sort_order is not None:
				url += '&sort_order=%s' % (sort_order)
			#url +=' order_by:updated_at sort:desc'

		return cls._get_model_execute(api, url=url, override='results', 
								method='query')

	@classmethod
	def _get_url_context(cls, method, *args, **kwargs):

		try:

			ids = kwargs.get('ids', None)
			if ids is not None and isinstance(ids, list):
				kwargs.update({
					'ids':','.join(str(i) for i in ids)
					})

			kwargs.update({
				'method':method,
				'model':cls.__name__.lower()
			})

			if hasattr(cls, '_relation') and cls._relation is not None:
				kwargs.update({
					'relation':cls._relation.__name__.lower()
				})

			url = kwargs.get('url', None)

			if url is None:

				mapped_url = cls._get_mapped_url(cls.__name__.lower(), method, 
						override_relation=kwargs.get('override_relation','default'))
				
				url = mapped_url.format(**kwargs)
				
				kwargs.update({
					'url':url
				})

			return kwargs

		except AttributeError as e:
			raise ModelEndpointException('reason: %s' % (e))

		except Exception as e:
			raise ModelException('reason: %s' % (e))

	def _put_url_context(self, method, *args, **kwargs):
		try:

			kwargs.update({
				'method':method,
				'model':self.__class__.__name__.lower(),
				'obj':self
			})

			if hasattr(self, '_relation') and self._relation is not None:
				kwargs.update({
					'relation':self._relation.__name__.lower()
				})

			sub_method = ('update' if self.id is not None else 'create')

			mapped_url = self._put_mapped_url(kwargs.get('model'), method, sub_method)

			if self.id is not None:
				kwargs.update({
					'id':self.id
					})
			url = mapped_url.format(**kwargs)

			kwargs.update({
				'url':url,
				'sub_method':sub_method
			})
			return kwargs

		except AttributeError as e:
			raise ModelEndpointException('reason: %s' % (e))

		except Exception as e:
			raise ModelException('reason: %s' % (e))

	def _delete_url_context(self, method, *args, **kwargs):
		try:

			kwargs.update({
				'method':method,
				'model':self.__class__.__name__.lower(),
				'obj':self,
				'id':self.id
			})

			if hasattr(self, '_relation') and self._relation is not None:
				kwargs.update({
					'relation':self._relation.__name__.lower()
				})

			mapped_url = self._delete_mapped_url(kwargs.get('model'), method)
			
			url = mapped_url.format(**kwargs)
			
			kwargs.update({
				'url':url
			})

			return kwargs

		except AttributeError as e:
			raise ModelEndpointException('reason: %s' % (e))

		except Exception as e:
			raise ModelException('reason: %s' % (e))

	def _put_model_execute(self, api, *args, **kwargs):

		override = kwargs.get('override', None)
		model = kwargs.get('model')
		if override is not None:
			model = override
		
		kwargs.update({
			'item_data':{
				 model:self.__dict__
				}
			})

		data = api._put_execute(*args, **kwargs)
		kwargs.update({'data':data})
		return api._put_parsed(**kwargs)

	def _delete_model_execute(self, api, *args, **kwargs):

		data = api._delete_execute(*args, **kwargs)
		
		kwargs.update({'data':data})

		api._delete_parsed(**kwargs)

	def delete(self, api, *args, **kwargs):

		method = inspect.stack()[0][3]
		kwargs = self._delete_url_context(method, *args, **kwargs)
		

		self._delete_model_execute(api, *args, **kwargs)

	def put(self, api, *args, **kwargs):

		method = inspect.stack()[0][3]
		kwargs = self._put_url_context(method, *args, **kwargs)

		return self._put_model_execute(api, *args, **kwargs)

	@classmethod
	def get(cls, api, *args, **kwargs):

		method = inspect.stack()[0][3]
		kwargs = cls._get_url_context(method, *args, **kwargs)
		return cls._get_model_execute(api, *args, **kwargs)

	@classmethod
	def fetch(cls, api, *args, **kwargs):
		#print kwargs.get('url')
		method = inspect.stack()[0][3]
		kwargs = cls._get_url_context(method, *args, **kwargs)

		return cls._get_model_execute(api, *args, **kwargs)
