from base import Model

class User(Model):

	def get_memberships(self, api, *args, **kwargs):

		kwargs = self._override_relation(**kwargs)
		return Group_Membership.fetch(api, user_id=self.id, **kwargs)

class User_Field(Model):

	pass

class Group(Model):

	def get_memberships(self, api, *args, **kwargs):

		kwargs = self._override_relation(**kwargs)
		return Group_Membership.fetch(api, group_id=self.id, **kwargs)

class Group_Membership(Model):

	_relation = None #dynamic relation

	@classmethod
	def fetch(cls, api, *args, **kwargs):
		"""
		In special cases where a fetch can work with
		multiple types of calls, we must override the fetch
		and change the relation, in order to preserve the initial fetch
		"""
		user_id = kwargs.get('user_id', None)
		group_id = kwargs.get('group_id', None)

		if user_id is not None:
			cls._relation = User

		elif group_id is not None:
			cls._relation = Group

		return super(Group_Membership, cls).fetch(api, *args, **kwargs)

class Custom_Role(Model):
	
	pass

class Identitie(Model):

	_relation = User

	def put(self, api, *args, **kwargs):
		kwargs.update({
			'override':'identity'
			})
		return super(Identitie, self).put(api, *args, **kwargs)

	@classmethod
	def get(cls, api, *args, **kwargs):
		kwargs.update({
			'override':'identity'
			})
		return super(Identitie, cls).get(api, *args, **kwargs)

	def delete(self, api, *args, **kwargs):
		kwargs.update({
			'override':'identity'
			})
		return super(Identitie, self).delete(api, *args, **kwargs)

