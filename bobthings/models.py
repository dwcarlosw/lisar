from django.db import models
from django.contrib.contenttypes import generic
from project_lisar.models import BaseModel, GenericFKMixin
from _misc.models import Comment
from django.contrib.auth.models import User
from jsonfield import JSONField
from django.contrib.contenttypes.models import ContentType

from mptt.models import TreeForeignKey

class Article( BaseModel ):
    # The user who requested this ticket
    publisher_id = models.ForeignKey(User, blank=True, null=True, related_name='%(app_label)s_%(class)s_publisher')
    title = models.CharField(max_length=100, blank=True, default='')
    article = models.TextField()

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)

    @property
    def comment(self):
        '''
        Because model Rule is subclassing GenericFKBaseModel
        and we do not simply have a ForeignKey to a Rule from a Todo
        we must get the Rule by querying Rules. For now, it will GenericForeignKey back to the Todo,
        with one Rule, but Todo might have multiple Rules in future
        '''
        try:
            return Comment.objects.get(content_type=self.model_content_type(),
                                        object_id=self.pk)
        except:
            return None


class SideNew( BaseModel ):
    title = models.CharField(max_length=100, blank=True, default='')
    article = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(SideNew, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.title


# class Comment( GenericFKMixin ):
#     """
#     Since it is using generic foreign key,
#     it requires "'content_type', 'object_id'" in fields of the CommentSerializer
#     """
#     # updated = models.DateTimeField(auto_now=True)
#     # created = models.DateTimeField(auto_now_add=True)
#     # #https://docs.djangoproject.com/en/dev/topics/db/models/#be-careful-with-related-name
#     # created_by = models.ForeignKey(User, blank=True, null=True, related_name='%(app_label)s_%(class)s_created')
#     # updated_by = models.ForeignKey(User, blank=True, null=True, related_name='%(app_label)s_%(class)s_updated')
#     text = models.TextField()
#
#     class Meta:
#         ordering = ('created',)




