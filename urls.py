from django.contrib import admin
admin.autodiscover()
from django.conf.urls import patterns, url, include
from bobthings import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'sidenew', views.SideNewViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    # url(r'^bobthings/$', views.IndexView.as_view()),
    #url(r'^bobthings/', include('bobthings.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )


urlpatterns += i18n_patterns('',
# urlpatterns += patterns('',
    url(r'^bobthings/$', include('bobthings.urls')),
    url(r'^translate/$', include('translate.urls')),
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