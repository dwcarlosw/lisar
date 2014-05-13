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
from bobthings.views import BobthingsView, IndexView, Comment

urlpatterns = patterns('bobthings.views',
    # url(r'^$', BobthingsView.as_view(), name='bobthings-index'),
    url(r'^$', IndexView.as_view(), name='bobthings-index'),
    # url(r'^add_comment/', Comment.as_view(), name="add-comment"),
    # url(r'^comment/', Comment.as_view(), name="refresh-comment"),
    # url(r'^comment/(?P<pk>[0-9]+)$', Comment.as_view(), name='comment-detail'),

)
