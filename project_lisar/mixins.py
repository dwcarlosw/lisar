from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.template.defaultfilters import slugify

class BaseMixin(models.Model):
    '''
    This contains all of the common fields.
    '''

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    #https://docs.djangoproject.com/en/dev/topics/db/models/#be-careful-with-related-name
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='%(app_label)s_%(class)s_created')
    updated_by = models.ForeignKey(User, blank=True, null=True, related_name='%(app_label)s_%(class)s_updated')


    class Meta:
        abstract = True
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(BaseMixin, self).save(*args, **kwargs)

    @property
    def model_content_type(self):
        return ContentType.objects.get_for_model(self)

    @property
    def model_content_type_id(self):
        return self.model_content_type.id

    @property
    def model_content_type_name(self):
        return self.model_content_type.model_class().__name__

class GenericFKMixin(BaseMixin):
    '''
    Generic foreignkey fields as per: https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/#generic-relations
    '''

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


