from django.conf.urls import patterns, url, include
from translate import views



# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
   url(r'^', 'translate.views.index'),
)

