from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.http import Http404
from django.shortcuts import render_to_response

def index(request):
    # HTTP_ACCEPT_LANGUAGE
    for k in request.META:
        print k, ':', request.META[k]
    print request.META['HTTP_ACCEPT_LANGUAGE']
    data = _('Hello')
    return render_to_response('translate.html', {'context': data})