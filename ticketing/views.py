from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, permissions
from rest_framework.renderers import YAMLRenderer, JSONRenderer


from drf_ujson.renderers import UJSONRenderer


from models import Ticket
from permissions import IsOwnerOrReadOnly
from serializer import TicketSerializer, UserSerializer
from renderers import TicketsRenderer
# Create your views here.


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly,)
    # renderer_classes = (UJSONRenderer, TicketsRenderer)
    renderer_classes = (JSONRenderer, TicketsRenderer)
    #
    # def list(self, request, *args, **kwargs):
    #     response = super(TicketViewSet, self).list(request, *args, **kwargs)
    #     if request.accepted_renderer.format == 'html':
    #         return Response({'': response.data}, template_name='index.html')
    #     return response
    def pre_save(self, obj):
         obj.owner = self.request.user