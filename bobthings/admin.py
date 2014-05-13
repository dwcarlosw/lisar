from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from models import Article, SideNew, Comment
from project_lisar.models import Alternate
from project_lisar.admin import BaseModelAdmin
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

class CommentAdmin(BaseModelAdmin, BaseTranslationAdmin, CompareVersionAdmin):
    # list_display = ('name', 'code',)
    pass

class ArticleAdmin(DjangoMpttAdmin, BaseTranslationAdmin, CompareVersionAdmin):
    pass

class SideNewAdmin(DjangoMpttAdmin, BaseTranslationAdmin, CompareVersionAdmin):
    pass

class AlternateAdmin(BaseTranslationAdmin, CompareVersionAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(SideNew, SideNewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Alternate, AlternateAdmin)




