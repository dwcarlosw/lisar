from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mixins import BaseMixin, GenericFKMixin
from jsonfield import JSONField
from django.core.exceptions import ValidationError
from django.db.models.fields import FieldDoesNotExist
import json


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


class Alternate(GenericFKMixin):
    values = JSONField()

    text = models.TextField()

    def clean(self):

        non_valid_fields = []
        for k, v in self.values.iteritems():
            if k not in self.content_object._meta.get_all_field_names():
                non_valid_fields.append(k)

        #If there are ANY non valid fields, the entire save is aborted via this exception
        if non_valid_fields:
            raise ValidationError('The following fields does not exist on %s: %s'% (
                self.content_object._meta.object_name,
                non_valid_fields
            ))

        #If all fields are valid, check the field types first...
        non_valid_types = ['ForeignKey', 'ManyToManyField', 'OneToOneField']
        non_valid_map = []

        for k in self.values.keys():
            _content_object = self.content_object
            if _content_object._meta.get_field(k).get_internal_type() in non_valid_types:
                non_valid_map.append(k)

        if non_valid_map:
            raise ValidationError('%s not accepted in the Alternate model.' % non_valid_map)

        '''
        Validation for unique key-values within the content_type
        ex. 	'United' --> USA and 'United' --> UK would be disaster for a lookup of
                USA._all_values('name'). It would return an overlapping value with UK._all_values('name'),
                causing a matching error for our importer or other things that rely on the Alternate model.
        '''


        found_overlapping = False

        # alternates = Alternate.objects.filter(content_type=self.content_type,
        #                     object_id=self.object_id)
        # for alternate in alternates:
        #     for k, v in alternate.values.iteritems():
        #         for j, l in self.values.iteritems():
        #             if k == j and v == l:
        #                 found_overlapping = True
        #                 break

        alts = Alternate.objects.filter( content_type=self.content_type,
                                         values__contains=json.dumps(self.values,separators=(',',':'))[1:-1] )
        if alts:
            found_overlapping = True

        if found_overlapping:
            raise ValidationError('Overlapping values found')


    def save(self, *args, **kwargs):
        self.clean()
        super(Alternate, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)