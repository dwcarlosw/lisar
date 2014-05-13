from django.contrib import admin
from _base.admin import *
from models import *
from django_mptt_admin.admin import DjangoMpttAdmin
from modeltranslation.admin import TranslationAdmin
import reversion
from reversion_compare.admin import CompareVersionAdmin


# Register your models here.


class BaseTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class BaseAdmin( BaseTranslationAdmin, BaseModelAdmin, CompareVersionAdmin, DjangoMpttAdmin ):
    pass



class TicketAdmin(BaseAdmin):
    pass
# class CommentAdmin(BaseAdmin):
#     pass
class BrandAdmin(BaseAdmin):
    pass
class GroupAdmin(BaseAdmin):
    pass
class GroupMembershipAdmin(BaseAdmin):
    pass
class OrganizationFieldAdmin(BaseAdmin):
    pass
class TicketFieldAdmin(BaseAdmin):
    pass
class TicketFormsAdmin(BaseAdmin):
    pass
class SatisfactionAdmin(BaseAdmin):
    pass
class SharingAgreementAdmin(BaseAdmin):
    pass
class TicketViewsAdmin(BaseAdmin):
    pass
class TicketAuditAdmin(BaseAdmin):
    pass
class TicketMetricAdmin(BaseAdmin):
    pass
class UserdbAdmin(BaseAdmin):
    pass

# admin.site.register(Comment, CommentAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(GroupMembership, GroupMembershipAdmin)
admin.site.register(OrganizationField, OrganizationFieldAdmin)
admin.site.register(TicketField, TicketFieldAdmin)
admin.site.register(TicketForms, TicketFormsAdmin)
admin.site.register(Satisfaction, SatisfactionAdmin)
admin.site.register(SharingAgreement, SharingAgreementAdmin)
admin.site.register(TicketViews, TicketViewsAdmin)
admin.site.register(TicketAudit, TicketAuditAdmin)
admin.site.register(TicketMetric, TicketMetricAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(userdb, UserdbAdmin)