import os
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from mixins import BaseMixin, GenericFKMixin

class BaseMPTTModel(MPTTModel):
    '''
    This contains MPTT functionality.
    '''
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')

    class Meta:
        abstract = True

class BaseModel(BaseMPTTModel, BaseMixin):
    pass
    class Meta:
        abstract = True

class GenericFKBaseModel(BaseModel, GenericFKMixin):
    pass
    class Meta:
        abstract = True
