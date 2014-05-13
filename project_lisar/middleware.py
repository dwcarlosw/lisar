from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr.lstrip('/')) for expr in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).

    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required middleware\
 requires authentication middleware to be installed. Edit your\
 MIDDLEWARE_CLASSES setting to insert\
 'django.contrib.auth.middlware.AuthenticationMiddleware'. If that doesn't\
 work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
 'django.core.context_processors.auth'."
        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL)



from django.http import HttpResponseRedirect
from django.conf import settings
import re

class EnforceLoginMiddleware(object):
    """
    Middlware class which requires the user to be authenticated for all urls except
    those defined in PUBLIC_URLS in settings.py. PUBLIC_URLS should be a tuple of regular
    expresssions for the urls you want anonymous users to have access to. If PUBLIC_URLS
    is not defined, it falls back to LOGIN_URL or failing that '/accounts/login/'.
    Requests for urls not matching PUBLIC_URLS get redirected to LOGIN_URL with next set
    to original path of the unauthenticted request.
    Any urls statically served by django are excluded from this check. To enforce the same
    validation on these set SERVE_STATIC_TO_PUBLIC to False.
    """

    def __init__(self):
        self.login_url   = getattr(settings, 'LOGIN_URL', '/api-auth/login/' )
        if hasattr(settings,'PUBLIC_URLS'):
            public_urls = [re.compile(url) for url in settings.PUBLIC_URLS]
        else:
            public_urls = [(re.compile("^%s$" % ( self.login_url[1:] )))]
        # if getattr(settings, 'SERVE_STATIC_TO_PUBLIC', True ):
        #     root_urlconf = __import__(settings.ROOT_URLCONF)
        #     public_urls.extend([ re.compile(url.regex)
        #         for url in root_urlconf.urls.urlpatterns
        #         if url.__dict__.get('_callback_str') == 'django.views.static.serve'
        #     ])
        self.public_urls = tuple(public_urls)

    def process_request(self, request):
        """
        Redirect anonymous users to login_url from non public urls
        """
        try:
            if request.user.is_anonymous():
                for url in self.public_urls:
                    if url.match(request.path[1:]):
                        return None
                return HttpResponseRedirect("%s?next=%s" % (self.login_url, request.path))
        except AttributeError:
            return HttpResponseRedirect("%s?next=%s" % (self.login_url, request.path))