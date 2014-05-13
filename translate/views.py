from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.http import Http404
from django.shortcuts import render_to_response
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField
    sender = forms.EmailField
    cc_myself = forms.BooleanField(required=False)


def index(request):
    # HTTP_ACCEPT_LANGUAGE
    for k in request.META:
        print k, ':', request.META[k]
    print request.META['HTTP_ACCEPT_LANGUAGE']
    data = _('Hello')
    form = ContactForm()
    return render_to_response('translate.html', {'context': data, 'form':form})