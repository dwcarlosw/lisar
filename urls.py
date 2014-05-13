from django.contrib import admin
import xadmin
from xadmin.plugins import xversion
admin.autodiscover()
xadmin.autodiscover()
from django.conf.urls import patterns, url, include
from bobthings import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

xversion.register_models()

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'sidenew', views.SideNewViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'comment', views.CommentViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    # url(r'^bobthings/$', views.IndexView.as_view()),
    #url(r'^bobthings/', include('bobthings.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

urlpatterns += i18n_patterns('',
# urlpatterns += patterns('',
    url(r'^bobthings/', include('bobthings.urls')),
    url(r'^translate/$', include('translate.urls')),
    url(r'^ticketing/', include('ticketing.urls')),

)






#
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'LISAR.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     url(r'^$', include('bobthings.urls')),
#     url(r'^bobthings/', include('bobthings.urls')),
#     url(r'^admin/', include(admin.site.urls)),
#     # url(r'^comments/', include('django.contrib.comments.urls')),
# )