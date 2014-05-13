from rest_framework import serializers
from django.contrib.auth.models import User
from models import Ticket



class UserSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id',)

class TicketSerializer(serializers.ModelSerializer):
    created_by = serializers.Field(source='created_by.username')

    class Meta:
        model = Ticket
        # fields = ('id', 'type', 'subject', 'description', 'priority', 'status', 'recipient', 'requester_id',
        #           'submitter_id', 'assignee_id', 'organization_id', 'group_id', 'collaborator_ids', 'has_incidents',
        #           'due_at', 'satisfaction_rating', 'sharing_agreement_ids', 'followup_ids', 'ticket_form_id',
        #           'brand_id')
        fields = ('id', 'status', 'requester_id', 'subject', 'updated', 'priority', 'type', 'assignee_id')