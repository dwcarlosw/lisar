#from django.conf.urls.defaults import *
# from django.conf.urls import patterns
# from django.conf.urls.static import static
#
# patts =(  '',
#         (r'^$', 'bobthings.views.index'),
#
# )
#
# patts += ( (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': '/home/lisar/LISAR/bobthings/static'}), )
#
#
# urlpatterns = patterns( *patts )




from django.conf.urls import patterns, url
from bobthings.views import BobthingsView, IndexView

urlpatterns = patterns('bobthings.views',
    # url(r'^$', BobthingsView.as_view(), name='bobthings-index'),
    url(r'^$', IndexView.as_view(), name='bobthings-index'),

)
