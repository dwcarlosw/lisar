from modeltranslation.translator import translator, TranslationOptions
from models import *

class UserdbTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class TicketTranslationOptions(TranslationOptions):
    fields = ('subject', 'description',)
    required_languages = ('en', 'fr')
class OrganizationTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class BrandTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class GroupTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class GroupMembershipTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class OrganizationFieldTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
# class CommentTranslationOptions(TranslationOptions):
#     fields = ()
#     required_languages = ('en', 'fr')
class TicketFieldTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class TicketFormsTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class SatisfactionTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class SharingAgreementTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class TicketViewsTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class TicketAuditTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')
class TicketMetricTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('en', 'fr')

translator.register(Ticket, TicketTranslationOptions)
translator.register(Organization, OrganizationTranslationOptions)
translator.register(Brand, BrandTranslationOptions)
translator.register(Group, GroupTranslationOptions)
translator.register(GroupMembership, GroupMembershipTranslationOptions)
translator.register(OrganizationField, OrganizationFieldTranslationOptions)
# translator.register(Comment, CommentTranslationOptions)
translator.register(TicketField, TicketFieldTranslationOptions)
translator.register(TicketForms, TicketFormsTranslationOptions)
translator.register(Satisfaction, SatisfactionTranslationOptions)
translator.register(SharingAgreement, SharingAgreementTranslationOptions)
translator.register(TicketViews, TicketViewsTranslationOptions)
translator.register(TicketAudit, TicketAuditTranslationOptions)
translator.register(TicketMetric, TicketMetricTranslationOptions)
translator.register(userdb, UserdbTranslationOptions)