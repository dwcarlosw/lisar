from base import Model
from views import View

class Ticket(Model):

	_relation = None

	def get_audits(self, api, *args, **kwargs):
		
		return Audit.fetch(api, ticket_id=self.id)
	
	def get_comments(self, api, *args, **kwargs):

		return Comment.fetch(api, ticket_id=self.id)

	@classmethod
	def fetch(cls, api, *args, **kwargs):

		view_id = kwargs.get('view_id', None)
		if view_id is not None:
			cls._relation = View

		return super(Ticket, cls).fetch(api, *args, **kwargs)

class Ticket_Metric(Model):

	pass

class Comment(Model):

	_relation = Ticket

class Audit(Model):
	_relation = Ticket

class Ticket_Form(Model):

	def get_fields(self, api, *args, **kwargs):
		"""
		A workaround since no call exists to get ticket fields for a certain form
		- this will just return a list, with no helper object
		- this also helps with optimization
		"""
		fields = Ticket_Field.fetch(api, *args, **kwargs)
		items = []
		for field_id in self.ticket_field_ids:
			for field in fields.all():
				if field_id == field.id:
					items.append(field)
					break
		
		return items

class Ticket_Field(Model):
	
	pass