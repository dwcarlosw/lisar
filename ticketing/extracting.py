import sys, os, psycopg2, datetime
os.environ['PYTHONPATH'] = '/home/lisar/lisar'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from datetime import date
from zendesk_api_v2.zendesk_api import ZendeskAPI
from zendesk_api_v2.tickets import Ticket as APITicket
from zendesk_api_v2.users import User as APIUser
from zendesk_api_v2.organizations import Organization as APIOrganizations
from zendesk_api_v2.group import Group as APIGroup
from zendesk_api_v2.users import Group_Membership as APIGroup_Membership

from zendesk_api_v2.base import Model

from django.contrib.auth.models import User
from django.db import transaction

from ticketing.models import Ticket
from ticketing.models import *

print os.environ['LOCAL_DB_USER']
print os.environ['LOCAL_DB_PASS']



class Fields_Base(object):
    def __init__(self):
        self.api = None
        self.model = None

        self.bf={
            'name':'',
            'created':datetime.datetime.now(),
            'updated':datetime.datetime.now()
        }
        self.fields = {}
        self.FKfs = []
        self.GFKfs = []
        self.M2Mfs = []

    def all_fields(self, api_obj):
        self.bf={
            'name':api_obj.name,
            'created':api_obj.created_at,
            'updated':api_obj.updated_at
        }

        fields = {}

        for f in self.fields:
            fields[f] = getattr(api_obj, f)

        fds = self.bf
        fds = dict(fds.items()+fields.items())

        return fds

    def sync(self):

        with transaction.atomic():
            if not self.api or not self.model:
                raise Exception("API or Model is not defined.")

            data = Fields_Base.extract_data(self.api)

            if not data:
                raise Exception("Extracting data...failed.")

            for t in data:

                fields = self.all_fields(t)

                exist = self.model.objects.filter(zdsk_id = t.id).count()

                if exist:
                    self.model.objects.filter(zdsk_id=t.id).update( **fields )
                    continue

                grp = self.model( **fields )

                grp.save()

    @staticmethod
    def extract_data( API ):

        AGENT_USER = 'oleg.p@broadconnect.ca'
        #URL = 'https://broadconnectusa.zendesk.com'

        # ID = 303877429

        AGENT_PASSWORD = 'Kop721suk'

        profile_data = {'url': u'https://broadconnect1.zendesk.com', 'token': u'Kop721suk', 'email': u'oleg.p@broadconnect.ca'}

        api = ZendeskAPI(user=profile_data['email'],
                        password=profile_data['token'],
                        url=profile_data['url'])

        try:
            data = []
            api_data = None
            while True:
                if api_data is None:
                    api_data = API.query(api)

                for t in api_data.all():
                    data.append(t)
                if not api_data.has_next():
                    break
                break
                api_data = api_data.next(api)
        except Exception, e:
            print "Error when accessing API call, ", e
            return None

        return data





class Fields_organization(Fields_Base):
    def __init__(self, api_obj):
        super(Fields_organization, self).__init__()

        self.model = Organization
        self.api = APIOrganizations

        self.fields = [ 'details','notes','shared_tickets','shared_comments' ]

        self.FKfs=['group_id']
        self.M2Mfs=['organization_fields']

class Fields_group(Fields_Base):
    def __init__(self):
        super(Fields_group, self).__init__()

        self.model = Group
        self.api = APIGroup

        self.fields =['deleted']

class Fields_group_membership(Fields_Base):
    def __init__(self, api_obj):
        super(Fields_group_membership, self).__init__()

        self.model = GroupMembership
        self.api = APIGroup_Membership

        self.fields =['default']
        self.FKfs=['user_id','group_id']

class Fields_organization_field(Fields_Base):
    def __init__(self, api_obj):
        super(Fields_organization_field, self).__init__()

        self.fields =['type','title','description','active','system','regexp_for_validation']
        self.FKfs=['user_id','group_id']

class Fields_ticket_field(Fields_Base):
    def __init__(self, api_obj):
        super(Fields_ticket_field, self).__init__()

        self.fields =['type','title','description','active','required','regexp_for_validation','title_in_portal',
                      'visible_in_portal','editable_in_portal','required_in_portal','removable']
        self.M2Mfs=['collapsed_for_agents']

class Fields_ticket_forms(Fields_Base):
    def __init__(self, api_obj):
        super(Fields_ticket_forms, self).__init__()

        self.fields =['display_name','active','end_user_visible','default']
        self.M2Mfs=['ticket_field_ids']


class Fields_ticket(Fields_Base):
    def __init__(self, api_obj):
        super(Fields_ticket, self).__init__()

        self.fields =['display_name','active','end_user_visible','default']
        self.M2Mfs=['ticket_field_ids']






fg = Fields_group()
fg.sync()

def Sync_Main():
    # Sync all data

    # Sync all FK

    # Sync all GFK

    # Sync all M2M

    pass