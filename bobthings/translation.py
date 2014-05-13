from modeltranslation.translator import translator, TranslationOptions
from models import Article, SideNew, Comment
from project_lisar.models import Alternate

class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'article',)
    required_languages = ('en', 'fr', 'zh-cn')


class SideNewTranslationOptions(TranslationOptions):
    fields = ('title', 'article',)
    required_languages = ('en', 'fr', 'zh-cn')

class CommentTranslationOptions(TranslationOptions):
    fields = ('text',)
    required_languages = ('en', 'fr', 'zh-cn')

translator.register(Article, ArticleTranslationOptions)
translator.register(SideNew, SideNewTranslationOptions)
translator.register(Comment, CommentTranslationOptions)


class AlternateTranslationOptions(TranslationOptions):
    fields = ( )
    required_languages = ('en', 'fr', 'zh-cn')
translator.register(Alternate, AlternateTranslationOptions)