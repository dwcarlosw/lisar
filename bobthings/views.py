from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from bobthings.models import Article, SideNew
from bobthings.serializer import ArticleSerializer,SideNewSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import viewsets
from rest_framework import permissions
from bobthings.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import link
from rest_framework import renderers
from django.contrib.auth.models import User
from bobthings.serializer import UserSerializer
from functools import wraps
from django.views.decorators.cache import patch_cache_control
import itertools


from django.utils.translation import ugettext as _


#django_rosetta

def never_cache(decorated_function):
	'''
	Removes view caching
	'''
	@wraps(decorated_function)
	def wrapper(*args, **kwargs):
		response = decorated_function(*args, **kwargs)
		patch_cache_control(
		response, no_cache=True, no_store=True, must_revalidate=True,
			max_age=0)
		return response
	return wrapper



@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly,)
    # renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    #
    # def list(self, request, *args, **kwargs):
    #     response = super(ArticleViewSet, self).list(request, *args, **kwargs)
    #     if request.accepted_renderer.format == 'html':
    #         return Response({'articles': response.data}, template_name='index.html')
    #     return response
    def pre_save(self, obj):
         obj.owner = self.request.user


class SideNewViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = SideNew.objects.all()
    serializer_class = SideNewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    #
    # def list(self, request, *args, **kwargs):
    #     response = super(SideNewViewSet, self).list(request, *args, **kwargs)
    #     if request.accepted_renderer.format == 'html':
    #         return Response({'articles': response.data}, template_name='index.html')

    def pre_save(self, obj):
        obj.owner = self.request.user

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from models import *
from itertools import chain

class IndexView(ListAPIView):

    # context_object_name = "articles"
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        articles = Article.objects.all()
        sidenews = SideNew.objects.all()

        results = {"articles":[], "sidenews":[], "trans":_("Hello there.")}

        entries = list(chain(articles, sidenews)) # combine the two querysetss
        for entry in entries:
            #type = entry.__class__.__name__.lower() # 'nurse', 'pilot'
            if isinstance(entry, Article):
                serializer = ArticleSerializer(entry)
                results["articles"].append( serializer.data )
            if isinstance(entry, SideNew):
                serializer = SideNewSerializer(entry)
                results["sidenews"].append( serializer.data )

        return Response({"results":results},template_name='index.html')


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


from django.views.generic import View, TemplateView, ListView
from django.utils.decorators import method_decorator

class BobthingsView(ListView):

    template_name = 'index.html'
    context_object_name = 'results'

    def get_context_data(self, **kwargs):

        context = super(BobthingsView, self).get_context_data(**kwargs)
        context.update({'items_per_page':self.paginate_by})
        return context

    def get_queryset(self):
        articles = Article.objects.all()
        articles.order_by('id')
        sidenews = SideNew.objects.all()
        sidenews.order_by('id')

        query= {"articles": articles,
                "sidenews": sidenews}

        return query

	def get_paginate_by(self, queryset):

		self.paginate_by = self.request.GET.get('limit', 20)
		return self.paginate_by

	@method_decorator(never_cache)
	def get(self, request, *args, **kwargs):
		return super(BobthingsView, self).get(request, *args, **kwargs)


# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
#
# @csrf_exempt
# def news_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = News.objects.all()
#         serializer = NewsSerializer(snippets, many=True)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = NewsSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def news_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         news = News.objects.get(pk=pk)
#     except news.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = NewsSerializer(news)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = NewsSerializer(news, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         news.delete()
#         return HttpResponse(status=204)




# from django.shortcuts import render
# from django.shortcuts import render_to_response, get_object_or_404
# # Create your views here.
#
#
# def index(request):
#     al = ["Welcome","To","bobthings"]
#     return render_to_response('index.html', {'al': al} )