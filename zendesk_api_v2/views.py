from base import Model
import tickets
from users import User

class View(Model):
	@classmethod
	def fetch(cls, api, *args, **kwargs):

		items = super(View, cls).fetch(api, *args, **kwargs)
		ids = [str(item.id) for item in items.all()]
		"""
		Update the view count for the view
		"""
		view_counts = View_Count.fetch(api, ids=ids)

		for view_count in view_counts.all():
			item = api._get_object_by_id(items.all(), view_count.view_id)
			item.update(view_count=view_count.value)
		
		return items

	def get_tickets(self, api, *args, **kwargs):

		fetch = tickets.Ticket.fetch(api, view_id=self.id, 
								override_relation='view')

		"""
		TODO: build URL with include/sideloaded request parameters? Not necessary, but could be useful
		if many other views will use it
		"""

		sideloaded = fetch.get_sideloaded()

		"""
		This handles sideloaded results
		- this is to load in everything at once
		- as a method of optimization
		"""

		users = sideloaded.get('users', [])
		users_list = []
		
		for user in users:
			users_list.append(User(**user))

		for ticket in fetch.all():
			requester = api._get_object_by_id(users_list, ticket.requester_id)
			assignee = api._get_object_by_id(users_list, ticket.assignee_id)
		
			ticket.requester = requester
			ticket.assignee = assignee

		return fetch

class View_Count(Model):
	
	_relation = View