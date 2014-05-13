from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from _base.models import BaseModel, GenericFKBaseModel
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from ckeditor.fields import RichTextField

'''
These models are very generic models, but should nevertheless exist
outside of the _base app
'''

class Attachment(GenericFKBaseModel):
    file = FilerFileField()

    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')

class Image(GenericFKBaseModel):
    file = FilerImageField()

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

class RichTextSnippet(GenericFKBaseModel):
    text = RichTextField()

    class Meta:
        verbose_name = _('Rich Text Snippet')
        verbose_name_plural = _('Rich Text Snippets')

class Comment(GenericFKBaseModel):
    text = models.TextField()

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class Tag(GenericFKBaseModel):
    tag = models.CharField(max_length=10)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tag')