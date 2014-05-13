# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table(u'ticketing_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_organization_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_organization_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.Organization'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('shared_tickets', self.gf('django.db.models.fields.BooleanField')()),
            ('shared_comments', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'ticketing', ['Organization'])

        # Adding model 'Brand'
        db.create_table(u'ticketing_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_brand_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_brand_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.Brand'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'ticketing', ['Brand'])

        # Adding model 'Group'
        db.create_table(u'ticketing_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_group_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_group_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.Group'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ticketing', ['Group'])

        # Adding model 'GroupMembership'
        db.create_table(u'ticketing_groupmembership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_groupmembership_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_groupmembership_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.GroupMembership'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ticketing.userdb'])),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ticketing', ['GroupMembership'])

        # Adding model 'OrganizationField'
        db.create_table(u'ticketing_organizationfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_organizationfield_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_organizationfield_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.OrganizationField'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('system', self.gf('django.db.models.fields.BooleanField')()),
            ('regexp_for_validation', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'ticketing', ['OrganizationField'])

        # Adding model 'TicketField'
        db.create_table(u'ticketing_ticketfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticketfield_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticketfield_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.TicketField'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('required', self.gf('django.db.models.fields.BooleanField')()),
            ('regexp_for_validation', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title_in_portal', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('visible_in_portal', self.gf('django.db.models.fields.BooleanField')()),
            ('editable_in_portal', self.gf('django.db.models.fields.BooleanField')()),
            ('required_in_portal', self.gf('django.db.models.fields.BooleanField')()),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('removable', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'ticketing', ['TicketField'])

        # Adding M2M table for field collapsed_for_agents on 'TicketField'
        m2m_table_name = db.shorten_name(u'ticketing_ticketfield_collapsed_for_agents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticketfield', models.ForeignKey(orm[u'ticketing.ticketfield'], null=False)),
            ('userdb', models.ForeignKey(orm[u'ticketing.userdb'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ticketfield_id', 'userdb_id'])

        # Adding model 'TicketForms'
        db.create_table(u'ticketing_ticketforms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticketforms_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticketforms_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.TicketForms'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('end_user_visible', self.gf('django.db.models.fields.BooleanField')()),
            ('default', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'ticketing', ['TicketForms'])

        # Adding M2M table for field ticket_field_ids on 'TicketForms'
        m2m_table_name = db.shorten_name(u'ticketing_ticketforms_ticket_field_ids')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticketforms', models.ForeignKey(orm[u'ticketing.ticketforms'], null=False)),
            ('ticketfield', models.ForeignKey(orm[u'ticketing.ticketfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ticketforms_id', 'ticketfield_id'])

        # Adding model 'Ticket'
        db.create_table(u'ticketing_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticket_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticket_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.Ticket'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('subject_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('subject_fr', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('subject_zh_cn', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_zh_cn', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('recipient', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('requester_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticket_requester', null=True, to=orm['ticketing.userdb'])),
            ('submitter_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticket_submitter', null=True, to=orm['ticketing.userdb'])),
            ('assignee_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticket_assignee', null=True, to=orm['ticketing.userdb'])),
            ('organization_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticket_organization', null=True, to=orm['ticketing.Organization'])),
            ('group_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticket_group', null=True, to=orm['ticketing.Group'])),
            ('has_incidents', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('due_at', self.gf('django.db.models.fields.DateField')()),
            ('satisfaction_rating', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticket_satisfaction', null=True, to=orm['ticketing.Satisfaction'])),
            ('ticket_form_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticket_ticket_form', null=True, to=orm['ticketing.TicketForms'])),
            ('brand_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticket_brand', null=True, to=orm['ticketing.Brand'])),
        ))
        db.send_create_signal(u'ticketing', ['Ticket'])

        # Adding M2M table for field collaborator_ids on 'Ticket'
        m2m_table_name = db.shorten_name(u'ticketing_ticket_collaborator_ids')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticket', models.ForeignKey(orm[u'ticketing.ticket'], null=False)),
            ('userdb', models.ForeignKey(orm[u'ticketing.userdb'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ticket_id', 'userdb_id'])

        # Adding M2M table for field sharing_agreement_ids on 'Ticket'
        m2m_table_name = db.shorten_name(u'ticketing_ticket_sharing_agreement_ids')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticket', models.ForeignKey(orm[u'ticketing.ticket'], null=False)),
            ('sharingagreement', models.ForeignKey(orm[u'ticketing.sharingagreement'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ticket_id', 'sharingagreement_id'])

        # Adding M2M table for field followup_ids on 'Ticket'
        m2m_table_name = db.shorten_name(u'ticketing_ticket_followup_ids')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_ticket', models.ForeignKey(orm[u'ticketing.ticket'], null=False)),
            ('to_ticket', models.ForeignKey(orm[u'ticketing.ticket'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_ticket_id', 'to_ticket_id'])

        # Adding model 'Satisfaction'
        db.create_table(u'ticketing_satisfaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_satisfaction_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_satisfaction_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.Satisfaction'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('assignee_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_satisfaction_assignee', null=True, to=orm['ticketing.userdb'])),
            ('group_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_satisfaction_group', null=True, to=orm['ticketing.Group'])),
            ('requester_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_satisfaction_requester', null=True, to=orm['ticketing.userdb'])),
            ('ticket_id', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_satisfaction_ticket', null=True, to=orm['ticketing.Ticket'])),
            ('score', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_satisfaction_comment', null=True, to=orm['_misc.Comment'])),
        ))
        db.send_create_signal(u'ticketing', ['Satisfaction'])

        # Adding model 'SharingAgreement'
        db.create_table(u'ticketing_sharingagreement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_sharingagreement_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_sharingagreement_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.SharingAgreement'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'ticketing', ['SharingAgreement'])

        # Adding model 'Forum'
        db.create_table(u'ticketing_forum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_forum_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_forum_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.Forum'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'ticketing', ['Forum'])

        # Adding model 'TicketViews'
        db.create_table(u'ticketing_ticketviews', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticketviews_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticketviews_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.TicketViews'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'ticketing', ['TicketViews'])

        # Adding M2M table for field restriction on 'TicketViews'
        m2m_table_name = db.shorten_name(u'ticketing_ticketviews_restriction')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticketviews', models.ForeignKey(orm[u'ticketing.ticketviews'], null=False)),
            ('userdb', models.ForeignKey(orm[u'ticketing.userdb'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ticketviews_id', 'userdb_id'])

        # Adding model 'TicketAudit'
        db.create_table(u'ticketing_ticketaudit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticketaudit_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticketaudit_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.TicketAudit'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('ticket_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ticketing_ticketaudit_ticket', null=True, to=orm['ticketing.Ticket'])),
            ('author_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ticketing_ticketaudit_author', null=True, to=orm['ticketing.userdb'])),
        ))
        db.send_create_signal(u'ticketing', ['TicketAudit'])

        # Adding model 'TicketMetric'
        db.create_table(u'ticketing_ticketmetric', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticketmetric_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_ticketmetric_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.TicketMetric'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('ticket_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ticketing_ticketmetric_ticket', null=True, to=orm['ticketing.Ticket'])),
            ('group_stations', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('assignee_stations', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('reopens', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('replies', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('assignee_updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('requester_updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('status_updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('initially_assigned_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('assigned_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('solved_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('latest_comment_added_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('first_resolution_time_in_minutes', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('reply_time_in_minutes', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('full_resolution_time_in_minutes', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('agent_wait_time_in_minutes', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('requester_wait_time_in_minutes', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'ticketing', ['TicketMetric'])

        # Adding model 'userdb'
        db.create_table(u'ticketing_userdb', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_userdb_created', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ticketing_userdb_updated', null=True, to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['ticketing.userdb'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ticketing_userdb_ticket', unique=True, null=True, to=orm['auth.User'])),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('shared', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('shared_agent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('locale', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('time_zone', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('last_login_at', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('organization_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ticketing_userdb_organization', null=True, to=orm['ticketing.Organization'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('moderator', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ticket_restriction', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('only_private_comments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('suspended', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('restricted_agent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user_fields', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'ticketing', ['userdb'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table(u'ticketing_organization')

        # Deleting model 'Brand'
        db.delete_table(u'ticketing_brand')

        # Deleting model 'Group'
        db.delete_table(u'ticketing_group')

        # Deleting model 'GroupMembership'
        db.delete_table(u'ticketing_groupmembership')

        # Deleting model 'OrganizationField'
        db.delete_table(u'ticketing_organizationfield')

        # Deleting model 'TicketField'
        db.delete_table(u'ticketing_ticketfield')

        # Removing M2M table for field collapsed_for_agents on 'TicketField'
        db.delete_table(db.shorten_name(u'ticketing_ticketfield_collapsed_for_agents'))

        # Deleting model 'TicketForms'
        db.delete_table(u'ticketing_ticketforms')

        # Removing M2M table for field ticket_field_ids on 'TicketForms'
        db.delete_table(db.shorten_name(u'ticketing_ticketforms_ticket_field_ids'))

        # Deleting model 'Ticket'
        db.delete_table(u'ticketing_ticket')

        # Removing M2M table for field collaborator_ids on 'Ticket'
        db.delete_table(db.shorten_name(u'ticketing_ticket_collaborator_ids'))

        # Removing M2M table for field sharing_agreement_ids on 'Ticket'
        db.delete_table(db.shorten_name(u'ticketing_ticket_sharing_agreement_ids'))

        # Removing M2M table for field followup_ids on 'Ticket'
        db.delete_table(db.shorten_name(u'ticketing_ticket_followup_ids'))

        # Deleting model 'Satisfaction'
        db.delete_table(u'ticketing_satisfaction')

        # Deleting model 'SharingAgreement'
        db.delete_table(u'ticketing_sharingagreement')

        # Deleting model 'Forum'
        db.delete_table(u'ticketing_forum')

        # Deleting model 'TicketViews'
        db.delete_table(u'ticketing_ticketviews')

        # Removing M2M table for field restriction on 'TicketViews'
        db.delete_table(db.shorten_name(u'ticketing_ticketviews_restriction'))

        # Deleting model 'TicketAudit'
        db.delete_table(u'ticketing_ticketaudit')

        # Deleting model 'TicketMetric'
        db.delete_table(u'ticketing_ticketmetric')

        # Deleting model 'userdb'
        db.delete_table(u'ticketing_userdb')


    models = {
        u'_misc.comment': {
            'Meta': {'object_name': 'Comment'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'_misc_comment_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['_misc.Comment']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_zh_cn': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'_misc_comment_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ticketing.brand': {
            'Meta': {'object_name': 'Brand'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_brand_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.Brand']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_brand_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.forum': {
            'Meta': {'object_name': 'Forum'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_forum_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.Forum']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_forum_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.group': {
            'Meta': {'object_name': 'Group'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_group_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.Group']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_group_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.groupmembership': {
            'Meta': {'object_name': 'GroupMembership'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_groupmembership_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.GroupMembership']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_groupmembership_updated'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticketing.userdb']"})
        },
        u'ticketing.organization': {
            'Meta': {'object_name': 'Organization'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_organization_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.Organization']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'shared_comments': ('django.db.models.fields.BooleanField', [], {}),
            'shared_tickets': ('django.db.models.fields.BooleanField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_organization_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.organizationfield': {
            'Meta': {'object_name': 'OrganizationField'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_organizationfield_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.OrganizationField']"}),
            'regexp_for_validation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'system': ('django.db.models.fields.BooleanField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_organizationfield_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.satisfaction': {
            'Meta': {'object_name': 'Satisfaction'},
            'assignee_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_satisfaction_assignee'", 'null': 'True', 'to': u"orm['ticketing.userdb']"}),
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_satisfaction_comment'", 'null': 'True', 'to': u"orm['_misc.Comment']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_satisfaction_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'group_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_satisfaction_group'", 'null': 'True', 'to': u"orm['ticketing.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.Satisfaction']"}),
            'requester_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_satisfaction_requester'", 'null': 'True', 'to': u"orm['ticketing.userdb']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'score': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'ticket_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_satisfaction_ticket'", 'null': 'True', 'to': u"orm['ticketing.Ticket']"}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_satisfaction_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.sharingagreement': {
            'Meta': {'object_name': 'SharingAgreement'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_sharingagreement_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.SharingAgreement']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_sharingagreement_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.ticket': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Ticket'},
            'assignee_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_assignee'", 'null': 'True', 'to': u"orm['ticketing.userdb']"}),
            'brand_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_brand'", 'null': 'True', 'to': u"orm['ticketing.Brand']"}),
            'collaborator_ids': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_collaborator'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['ticketing.userdb']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_zh_cn': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'due_at': ('django.db.models.fields.DateField', [], {}),
            'followup_ids': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'followup_ids_rel_+'", 'null': 'True', 'to': u"orm['ticketing.Ticket']"}),
            'group_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_group'", 'null': 'True', 'to': u"orm['ticketing.Group']"}),
            'has_incidents': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'organization_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_organization'", 'null': 'True', 'to': u"orm['ticketing.Organization']"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.Ticket']"}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'recipient': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'requester_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_requester'", 'null': 'True', 'to': u"orm['ticketing.userdb']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'satisfaction_rating': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_satisfaction'", 'null': 'True', 'to': u"orm['ticketing.Satisfaction']"}),
            'sharing_agreement_ids': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_sharing_agreement'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['ticketing.SharingAgreement']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subject_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subject_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subject_zh_cn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'submitter_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_submitter'", 'null': 'True', 'to': u"orm['ticketing.userdb']"}),
            'ticket_form_id': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_ticket_form'", 'null': 'True', 'to': u"orm['ticketing.TicketForms']"}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticket_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.ticketaudit': {
            'Meta': {'object_name': 'TicketAudit'},
            'author_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ticketing_ticketaudit_author'", 'null': 'True', 'to': u"orm['ticketing.userdb']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticketaudit_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.TicketAudit']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'ticket_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ticketing_ticketaudit_ticket'", 'null': 'True', 'to': u"orm['ticketing.Ticket']"}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticketaudit_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.ticketfield': {
            'Meta': {'object_name': 'TicketField'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'collapsed_for_agents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'ticketing_ticketfield_collapsed_for_agents'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['ticketing.userdb']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticketfield_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'editable_in_portal': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.TicketField']"}),
            'regexp_for_validation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'removable': ('django.db.models.fields.BooleanField', [], {}),
            'required': ('django.db.models.fields.BooleanField', [], {}),
            'required_in_portal': ('django.db.models.fields.BooleanField', [], {}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title_in_portal': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticketfield_updated'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'visible_in_portal': ('django.db.models.fields.BooleanField', [], {})
        },
        u'ticketing.ticketforms': {
            'Meta': {'object_name': 'TicketForms'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticketforms_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'default': ('django.db.models.fields.BooleanField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'end_user_visible': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.TicketForms']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'ticket_field_ids': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'ticketing_ticketforms_ticket_fields'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['ticketing.TicketField']"}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticketforms_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.ticketmetric': {
            'Meta': {'object_name': 'TicketMetric'},
            'agent_wait_time_in_minutes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'assigned_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'assignee_stations': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'assignee_updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticketmetric_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'first_resolution_time_in_minutes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'full_resolution_time_in_minutes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'group_stations': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initially_assigned_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'latest_comment_added_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.TicketMetric']"}),
            'reopens': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'replies': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reply_time_in_minutes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'requester_updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'requester_wait_time_in_minutes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'solved_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'status_updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'ticket_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ticketing_ticketmetric_ticket'", 'null': 'True', 'to': u"orm['ticketing.Ticket']"}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticketmetric_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.ticketviews': {
            'Meta': {'object_name': 'TicketViews'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticketviews_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.TicketViews']"}),
            'restriction': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'ticketing_ticketviews_restriction'", 'null': 'True', 'to': u"orm['ticketing.userdb']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_ticketviews_updated'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ticketing.userdb': {
            'Meta': {'ordering': "('created',)", 'object_name': 'userdb'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_userdb_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'moderator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'only_private_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'organization_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ticketing_userdb_organization'", 'null': 'True', 'to': u"orm['ticketing.Organization']"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['ticketing.userdb']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'restricted_agent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'shared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shared_agent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'}),
            'suspended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ticket_restriction': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ticketing_userdb_updated'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ticketing_userdb_ticket'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_fields': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['ticketing']