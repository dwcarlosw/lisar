from django.db import models
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from _base.models import BaseModel, GenericFKBaseModel
from mptt.fields import TreeForeignKey, TreeOneToOneField, TreeManyToManyField
from _misc.models import Comment, Tag
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class DomainNames(GenericFKBaseModel):
    domain_name = models.CharField(max_length=200, blank=True, null=True)


class Organization(BaseModel):

    zdsk_id = models.IntegerField(blank=False)

    # New tickets from users in this organization will automatically be put in this group
    group_id = models.ForeignKey( 'ticketing.Group', blank=True, null=True, related_name='%(app_label)s_%(class)s_group_id')
    # Custom fields for this organization
    organization_fields = models.ManyToManyField('ticketing.OrganizationField', blank=True, null=True, related_name='%(app_label)s_%(class)s_organization_fields')

    # In this field you can store any details obout the organization. e.g. the address
    details = models.TextField(max_length=1000, blank=True, null=True)
    # In this field you can store any notes you have about the organization
    notes = models.TextField(max_length=1000, blank=True, null=True)
    # End users in this organization are able to see eachother's tickets
    shared_tickets = models.BooleanField(blank=False)
    # End users in this organization are able to see eachother's comments on tickets
    shared_comments = models.BooleanField(blank=False)



class Brand(BaseModel):
    pass

"""
When support requests arrive in Zendesk, they can be assigned to a Group.
Groups serve as the core element of ticket workflow;
support agents are organized into Groups and tickets can be assigned to a Group only,
or to an assigned agent within a Group.
A ticket can never be assigned to an agent without also being assigned to a Group.
"""
class Group(BaseModel):

    zdsk_id = models.IntegerField(blank=False)


    #Deleted groups get marked as such
    deleted = models.BooleanField(default=False)

"""
A membership links an agent to a group.
Groups can have many agents, as agents can be in many groups.
You can use the API to list what agents are in which groups, and reassign group members.
"""
class GroupMembership(BaseModel):

    zdsk_id = models.IntegerField(blank=False)


    # The id of an agent
    user_id = models.ForeignKey('ticketing.userdb', blank=True, null=True, related_name='%(app_label)s_%(class)s_user_id')
    # The id of a group
    group_id = models.ForeignKey('ticketing.Group', blank=True, null=True, related_name='%(app_label)s_%(class)s_group_id')

    # If true, tickets assigned directly to the agent will assume this membership's group.
    default = models.BooleanField(default=False)

"""
Zendesk allows admins to customize fields displayed on an Organization page.
Basic text fields, date fields, as well as customizable dropdown and number fields are available.
These fields are currently only visible to agents.
"""
class OrganizationField(BaseModel):

    zdsk_id = models.IntegerField(blank=False)


    TYPE_CHOICES=(('Text',"text"), ('Textarea',"textarea"), ('Checkbox',"checkbox"), ('Date',"date"), ('Integer',"integer"), ('Decimal',"decimal"), ('Regexp',"regexp"), ('Tagger',"tagger"))

    # # Optional for custom field of type "checkbox"; not presented otherwise.
    # tag = models.CharField(max_length=20)
    # position -- Ordering of the field relative to other fields , use self.parent

    # Supported types: "text", "textarea", "checkbox", "date", "integer", "decimal", "regexp", "tagger" (custom dropdown)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    # The title of the custom field
    title = models.CharField(max_length=50)
    # 	string	no	no	User-defined description of this field's purpose
    description = models.TextField(max_length=200)
    # If true, this field is available for use
    active = models.BooleanField(blank=False)
    # If true, only active and position values of this field can be changed
    system = models.BooleanField(blank=False)
    # Regular expression field only. The validation pattern for a field value to be deemed valid.
    regexp_for_validation = models.CharField(max_length=50)


    #######################################################
    # custom_field_options	array	no	yes	Required and presented for a custom field of type "tagger"
    # position	integer	no	no	Ordering of the field relative to other fields
    # key	string	no	on create	A unique key that identifies this custom field. This is used for updating the field and referencing in placeholders.
    #######################################################



"""
Zendesk allows admins to customize fields that display on the ticket form.
Basic text fields as well as customizable dropdown and number fields are available.
The visibility of these fields can be customized for end-users in the portal interface as well as to agent interfaces.
"""
class TicketField(BaseModel):

    zdsk_id = models.IntegerField(blank=False)


    # If this field should be shown to agents by default or be hidden alongside infrequently used fields
    collapsed_for_agents = models.ManyToManyField('ticketing.userdb', blank=True, null=True, related_name='%(app_label)s_%(class)s_collapsed_for_agents')

    # position -- A relative position for the ticket fields, determines the order of ticket fields on a ticket , use self.parent
    # # Optional for custom field of type "checkbox"; not presented otherwise.
    # tag = models.CharField(max_length=20)

    # The type of the ticket field
    type = models.CharField(max_length=50)
    # The title of the ticket field
    title = models.CharField(max_length=50)
    # The description of the purpose of this ticket field, shown to users
    description = models.TextField(max_length=200)
    # Whether this field is available
    active = models.BooleanField(blank=False)
    # If it's required for this field to have a value when updated by agents
    required = models.BooleanField(blank=False, default=False)
    # Regular expression field only. The validation pattern for a field value to be deemed valid.
    regexp_for_validation = models.CharField(max_length=50)
    # The title of the ticket field when shown to end users
    title_in_portal = models.CharField(max_length=50)
    # Whether this field is available to end users
    visible_in_portal = models.BooleanField(blank=False)
    # Whether this field is editable by end users
    editable_in_portal = models.BooleanField(blank=False)
    # If it's required for this field to have a value when updated by end users
    required_in_portal = models.BooleanField(blank=False, default=False)
    # If this field is not a system basic field that must be present for all tickets on the account
    removable = models.BooleanField()


    ############################################
    # system_field_options	array	yes	no	Presented for a ticket field of type "tickettype", "priority" or "status"
    # custom_field_options	array	no	yes	Required and presented for a ticket field of type "tagger"
    ############################################

"""
Ticket forms allow an admin to define a subset of ticket fields for display to both agents and end-users.
"""
class TicketForms(BaseModel):

    zdsk_id = models.IntegerField(blank=False)

    # The position of this form among other forms in the account, i.e. dropdown, providing by django mptt

    # ids of all ticket fields which are in this ticket form
    ticket_field_ids = models.ManyToManyField("ticketing.TicketField", blank=True, null=True, related_name='%(app_label)s_%(class)s_ticket_fields')

    # The name of the form that is displayed to an end user
    display_name = models.CharField(max_length=50)
    # If the form is set as active
    active = models.BooleanField()
    # Is the form visible to the end user
    end_user_visible = models.BooleanField()
    # Is the form the default form for this account
    default = models.BooleanField()




class Ticket(BaseModel):
    TYPE_CHOICES = (("Problem","problem"), ("Incident","incident"), ("Question","question"), ("Task","task"))
    PRIORITY_CHOICES = (('Urgent',"urgent"), ("High","high"), ("Normal","normal"), ("Low","low"))
    STATE_CHOICES = (('New',"new"), ("Open","open"), ("Pending","pending"), ("Hold","hold"), ("Solved","solved"), ("Closed","closed"))

    zdsk_id = models.IntegerField(blank=False)


    # The array of tags applied to this ticket
    #tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='%(app_label)s_%(class)s_created')

    # The user who requested this ticket
    requester_id = models.ForeignKey('ticketing.userdb', blank=True, null=True, related_name='%(app_label)s_%(class)s_requester')
    #The user who submitted the ticket; The submitter always becomes the author of the first comment on the ticket.
    submitter_id = models.ForeignKey('ticketing.userdb', blank=True, null=True, related_name='%(app_label)s_%(class)s_submitter')
    # What agent is currently assigned to the ticket
    assignee_id = models.ForeignKey('ticketing.userdb', blank=True, null=True, related_name='%(app_label)s_%(class)s_assignee')
    # The organization of the requester
    organization_id = models.ForeignKey('ticketing.Organization', blank=True, null=True, related_name='%(app_label)s_%(class)s_organization')
    # The group this ticket is assigned to
    group_id = models.ForeignKey(Group, blank=True, null=True, related_name='%(app_label)s_%(class)s_group')
    # The satisfaction rating of the ticket, if it exists, or the state of satisfaction, 'offered' or 'unoffered'
    satisfaction_rating = models.ForeignKey('ticketing.Satisfaction', blank=True, null=True, related_name='%(app_label)s_%(class)s_satisfaction')
    # The id of the ticket form to render for this ticket - only applicable for enterprise accounts
    ticket_form_id = models.ForeignKey('ticketing.TicketForms', blank=True, null=True, related_name='%(app_label)s_%(class)s_ticket_form')
    # The id of the brand this ticket is associated with - only applicable for enterprise accounts
    brand_id = models.ForeignKey('ticketing.Brand', blank=True, null=True, related_name='%(app_label)s_%(class)s_brand')

    # Who are currently CC'ed on the ticket
    collaborator_ids = models.ManyToManyField('ticketing.userdb', blank=True, null=True, related_name='%(app_label)s_%(class)s_collaborator')
    # The ids of the sharing agreements used for this ticket
    sharing_agreement_ids = models.ManyToManyField('ticketing.SharingAgreement', blank=True, null=True, related_name='%(app_label)s_%(class)s_sharing_agreement')
    # The ids of the followups created from this ticket - only applicable for closed tickets
    followup_ids = models.ManyToManyField("self", blank=True, null=True, related_name='%(app_label)s_%(class)s_followups')

    # The type of this ticket, i.e. "problem", "incident", "question" or "task"
    type = models.CharField(max_length = 20, choices=TYPE_CHOICES)
    # The value of the subject field for this ticket
    subject = models.CharField(max_length=200)
    # The first comment on the ticket
    description = models.TextField(max_length=1000)
    # Priority, defines the urgency with which the ticket should be addressed: "urgent", "high", "normal", "low"
    priority = models.CharField(max_length = 20, choices=PRIORITY_CHOICES)
    # The state of the ticket, "new", "open", "pending", "hold", "solved", "closed"
    status = models.CharField(max_length = 20, choices=STATE_CHOICES)
    # The original recipient e-mail address of the ticket
    recipient = models.EmailField(max_length=100)
    # Is true of this ticket has been marked as a problem, false otherwise
    has_incidents = models.BooleanField(default=True)
    # If this is a ticket of type "task" it has a due date. Due date format uses ISO 8601 format.
    due_at = models.DateField()




    # The topic this ticket originated from, if any
    # forum_topic_id = TreeForeignKey(Forum, blank=True, null=True, related_name='%(app_label)s_%(class)s_created')

    ############################################
    # problem_id The problem this incident is linked to, if any
    # custom_fields array The custom fields of the ticketfs
    # via 	Via This object explains how the ticket was created
    ############################################
    class Meta:
        ordering = ('created',)

"""
If you have enabled satisfaction ratings for your account, this end point allows you to quickly retrieve all ratings.
"""
class Satisfaction(BaseModel):
    SCORE_CHOICES = (('Offered',"offered"), ("Unoffered","unoffered"), ("Good","good"), ("Bad","bad"))

    # The id of agent assigned to at the time of rating
    assignee_id = models.ForeignKey('ticketing.userdb', blank=True, null=True, related_name='%(app_label)s_%(class)s_assignee')
    # The id of group assigned to at the time of rating
    group_id = models.ForeignKey('ticketing.Group', blank=True, null=True, related_name='%(app_label)s_%(class)s_group')
    # The id of ticket requester submitting the rating
    requester_id = models.ForeignKey('ticketing.userdb', blank=True, null=True, related_name='%(app_label)s_%(class)s_requester')
    # The id of ticket being rated
    ticket_id = models.ForeignKey('ticketing.Ticket', blank=True, null=True, related_name='%(app_label)s_%(class)s_ticket')
    # The rating: "offered", "unoffered", "good" or "bad"
    score = models.CharField(max_length = 20, choices=SCORE_CHOICES)
    # The comment received with this rating, if available
    comment = models.ForeignKey(Comment, blank=True, null=True, related_name='%(app_label)s_%(class)s_comment')

class SharingAgreement(BaseModel):
    TYPE_CHOICES = (("Inbound","inbound"), ("Outbound","outbound"))
    STATUS_CHOICES = (("Accepted","accepted"), ("Declined","declined"), ("Pending","pending"), ("Inactive","inactive"))

    # Can be one of the following: inbound, outbound
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    # Can be one of the following: accepted, declined, pending, inactive
    status = models.CharField(max_length=20, choices = STATUS_CHOICES)

    ############################################
    # 	string	Can be one of the following: jira, null
    ############################################

# ############### I think we don't need these models for now #######################
class Forum(BaseModel):
    # description	string	no	no	A description of the forum
    # category_id	integer	no	no	Category this forum is in
    # organization_id	integer	no	no	Organization this forum is restricted to
    # locale_id	integer	no	no	User locale id this forum is restricted to
    # locked	boolean	no	no	Whether this forum is locked such that new entries and comments cannot be made
    # unanswered_topics	integer	yes	no	Contains the number of unanswered questions if this forum's topics are questions.
    # position	integer	no	no	The position of this forum relative to other forums in the same category
    # forum_type	string	no	no	The type of the topics in this forum, valid values: "articles", "ideas" or "questions"
    # access	string	no	no	Who has access to this forum, valid values: "everybody", "logged-in users" or "agents only"
    # tags	array	no	no	Restrict access to end-users and organizations with all these tags
    pass

"""
A view consists of one or more conditions that define a collection of tickets to display.
If the conditions are met, the ticket is included in the view.
For example, a view can display all open tickets that were last updated more than 24 hours ago.
"""
class TicketViews(BaseModel):
    # The title of the view
    title = models.CharField(max_length=20, blank=False)
    # Useful for determining if the view should be displayed
    active = models.BooleanField(blank=False)
    # Who may access this account. Will be null when everyone in the account can access it.
    restriction = models.ManyToManyField('ticketing.userdb', blank=False, null=True, related_name='%(app_label)s_%(class)s_restriction')

    ###############################
    # sla_id	integer	If the view is for an SLA this is the id
    # execution	Execute	An object describing how the view should be executed
    # conditions	Conditions	An object describing how the view is constructed
    ###############################

"""
Audits are a read-only history of all updates to a ticket and the events that occur as a result of these updates.
When a Ticket is updated in Zendesk, we store an Audit.
Each Audit represents a single update to the Ticket, and each Audit includes a list of changes, such as:

Changes to ticket fields
Addition of a new comment
Addition or removal of tags
Notifications sent to Groups, Assignees, Requesters and CCs
"""
class TicketAudit(BaseModel):
    # The ID of the associated ticket
    ticket_id = models.ForeignKey('ticketing.Ticket', blank=False, null=True, related_name='%(app_label)s_%(class)s_ticket')

    # The user who created the audit
    author_id = models.ForeignKey('ticketing.userdb', blank=False, null=True, related_name='%(app_label)s_%(class)s_author')

    ############################################
    # events	array	yes	An array of the events that happened in this audit. See Audit Events
    # via	Via	yes	This object explains how this audit was created
    # metadata	hash	yes	Metadata for the audit, custom and system data
    ############################################


class TicketMetric(BaseModel):
    # Id of the associated ticket
    ticket_id = models.ForeignKey('ticketing.Ticket', blank=False, null=True, related_name='%(app_label)s_%(class)s_ticket')
    # Number of groups this ticket passed through
    group_stations = models.PositiveIntegerField(_("Order"), blank=True, null=True)
    # Number of assignees this ticket had
    assignee_stations = models.PositiveIntegerField(_("Order"), blank=True, null=True)
    # Total number of times the ticket was reopened
    reopens = models.PositiveIntegerField(_("Order"), blank=True, null=True)
    # Total number of times ticket was replied to
    replies = models.PositiveIntegerField(_("Order"), blank=True, null=True)
    # When the assignee last updated the ticket
    assignee_updated_at = models.DateTimeField(blank=True, null=True)
    # When the requester last updated the ticket
    requester_updated_at = models.DateTimeField(blank=True, null=True)
    # When the status was last updated
    status_updated_at = models.DateTimeField(blank=False, null=True)
    # When the ticket was initially assigned
    initially_assigned_at = models.DateTimeField(blank=True, null=True)
    # When the ticket was last assigned
    assigned_at = models.DateTimeField(blank=False, null=True)
    # When the ticket was solved
    solved_at = models.DateTimeField(blank=False, null=True)
    # When the latest comment was added
    latest_comment_added_at = models.DateTimeField(blank=False, null=True)
    # Number of minutes to the first resolution time inside and out of business hours
    first_resolution_time_in_minutes = models.PositiveIntegerField(_("Order"), blank=True, null=True)
    # Number of minutes to the first reply inside and out of business hours
    reply_time_in_minutes = models.PositiveIntegerField(_("Order"), blank=True, null=True)
    # Number of minutes to the full resolution inside and out of business hours
    full_resolution_time_in_minutes = models.PositiveIntegerField(_("Order"), blank=True, null=True)
    # Number of minutes the agent spent waiting inside and out of business hours
    agent_wait_time_in_minutes = models.PositiveIntegerField(_("Order"), blank=True, null=True)
    # Number of minutes the requester spent waiting inside and out of business hours
    requester_wait_time_in_minutes = models.PositiveIntegerField(_("Order"), blank=True, null=True)


class userdb(BaseModel):

    '''
    This table extends the 'auth_user' table built into django. It provides the
    extra fields required for the ticketing module as specified by the Zendesk API.
    auth_user contains the following:
        - id
        - username
        - first_name
        - last_name
        - password
        - email
        - is_staff
        - is_active
        - date_joined
        - is_superuser
        - last_last_login
    '''

    role_choices = (
        ('End-User', 'end-user'),
        ('Agent','agent'),
        ('Admin','admin'),
    )

    restriction_choices = (
        ('Groups','groups'),
        ('Assigned','assigned'),
        ('Requested','requested'),
    )

    #uses the ID field provided by django in Users as a foreign key
    user = models.ForeignKey(User, unique = True, blank=False, null=True, related_name='%(app_label)s_%(class)s_ticket')
    #the users url
    # url = models.SlugField(max_length = 200, blank = False)
    #Agents can have an alias that is displayed to end-users
    alias = models.CharField(max_length = 30, null=True)
    #The time the user was created
    # created_at = models.DateField(auto_now_add = True)
    #The time the user was last updated
    # updated_at = models.DateField(auto_now = True)
    #Users that have been deleted will have the value 'false' here
    active = models.BooleanField(default = False)
    #we verify whether the user is authentic or not
    verified = models.BooleanField(default = False)
    #if this user is shared from another account
    shared = models.BooleanField(default = False)
    #if this account is a shared agent account
    shared_agent = models.BooleanField(default = False, blank = False)
    #the local for this user
    locale = models.CharField(max_length = 10, blank = True)
    #the language identifier for this user
    # locale_id = models.IntegerField(blank = True)
    #the time-zone of the user
    time_zone = models.CharField(max_length = 50, blank = True)
    #a time stamp of when the user logged in last
    last_login_at = models.DateField(blank = True, null=True)
    #the primary phone number of the user
    phone = models.CharField(max_length = 10, blank=True, null=True)
    #the signature of the user (for agents and admins only)
    signature = models.CharField(max_length = 200, blank = True, null=True)
    #details about the user
    details = models.CharField(max_length = 200, blank = True, null=True)
    #notes about the user
    notes = models.CharField(max_length = 200, blank = True, null=True)
    #the id of the organization that the user is associated with
    organization_id = models.ForeignKey(Organization, blank=False, null=True, related_name='%(app_label)s_%(class)s_organization')
    #the role of the user (end-user, agent or admin)
    role = models.CharField(max_length = 50, blank = True, choices = role_choices)
    #the ole of the user if the user is an agent on the enterprise plan
    # custom_role_id = models.IntegerField(blank = True)
    #designates whether this user can moderate forums
    moderator = models.BooleanField(blank = False, default = False)
    #which tickets the user has access to (grous, assigned, organization, requested, null)
    ticket_restriction = models.CharField(max_length = 100, blank = False, choices = restriction_choices)
    #if true, this user can only create private comments
    only_private_comments = models.BooleanField(blank = False, default = False)
    #tickets from suspended users are also suspended and these users cannot login
    suspended = models.BooleanField(blank = False, default = False)
    #indicates any restrictions for agents
    restricted_agent = models.BooleanField(default = False, blank = False)
    #custom fields for the user
    user_fields = models.CharField(max_length=10)


    class Meta:
        ordering = ('created',)
