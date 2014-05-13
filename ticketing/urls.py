from django.conf.urls import patterns, include, url
from views import UserViewSet, TicketViewSet
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets, routers
from django.contrib.auth.models import User, Group
from django.conf import settings



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'auth$', auth_view),

)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
