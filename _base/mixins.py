import os
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager

class BaseMixin(models.Model):
    '''
    This contains all of the common fields.
    '''

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    #https://docs.djangoproject.com/en/dev/topics/db/models/#be-careful-with-related-name
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='%(app_label)s_%(class)s_created')
    updated_by = models.ForeignKey(User, blank=True, null=True, related_name='%(app_label)s_%(class)s_updated')

    order = models.PositiveIntegerField(_("Order"), blank=True, null=True)
    name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        ordering = ['-created']

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.slug = slugify(self.name)
        super(BaseMixin, self).save(*args, **kwargs)

    def __unicode__(self):
            return u'%s' % self.name


class GenericFKMixin(models.Model):
    '''
    Generic foreignkey fields as per: https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/#generic-relations
    '''

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True