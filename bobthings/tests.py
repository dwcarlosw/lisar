#from django.test import TestCase

# Create your tests here.
import sys
#from django.conf import settings
#from django.conf.urls import patterns, url
import rosetta.urls

# for p in sys.path:
#     print p

from django.conf import global_settings
from django.conf.urls import patterns, url

# try:
#     from django.conf.urls import patterns, url
# except ImportError:
#     from django.conf.urls.defaults import patterns, url
#
#
# urlpatterns = patterns('rosetta.views',
#     url(r'^$', 'home', name='rosetta-home'),
#     url(r'^pick/$', 'list_languages', name='rosetta-pick-file'),
#     url(r'^download/$', 'download_file', name='rosetta-download-file'),
#     url(r'^select/(?P<langid>[\w\-_\.]+)/(?P<idx>\d+)/$', 'lang_sel', name='rosetta-language-selection'),
#     url(r'^translate/$', 'translate_text', name='translate_text'),
# )

class Organization(object):
    name = ""
    country = ""


class Product(object):
    def __init__(self, id, org, name):
        self.id = id
        self.Organization = org
        self.name = name

class Alternate(object):
    def __init__(self, ct, id, field, value):
        self.content_type = ct
        self.object_id = id
        self.name_value = {field:value}


        if globals()[field] == Organization:
            print "invalid field"
            return



p = Product(0, Organization(), "broadconnect")


Alternate(p.__class__.__name__, p.id, "Organization", "BC")


a_name = Alternate(p.__class__.__name__, p.id, "name", "siptrunk")


