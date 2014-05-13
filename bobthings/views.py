from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from bobthings.models import Article, SideNew, Comment
from bobthings.serializer import ArticleSerializer,SideNewSerializer, CommentSerializer
from django.contrib.contenttypes.models import ContentType


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import viewsets
from rest_framework import permissions
from bobthings.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import link
from rest_framework import renderers
from django.contrib.auth.models import User
from bobthings.serializer import UserSerializer
from functools import wraps
from django.views.decorators.cache import patch_cache_control
from django.conf import settings
from django import forms

from django.http import Http404

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


class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)

    # renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    #
    # def list(self, request, *args, **kwargs):
    #     response = super(SideNewViewSet, self).list(request, *args, **kwargs)
    #     if request.accepted_renderer.format == 'html':
    #         return Response({'articles': response.data}, template_name='index.html')

    def pre_save(self, obj):
        obj.created_by = self.request.user
        obj.owner = self.request.user


class CommentForm(forms.Form):
    comment = forms.CharField()

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from models import *
from itertools import chain

class IndexView(ListAPIView):

    # context_object_name = "articles"
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        articles = Article.objects.order_by("-created")
        sidenews = SideNew.objects.order_by("-created")

        if request.user.is_authenticated():
            user = request.user.username
        else:
            user = ""

        article_type = ContentType.objects.get_for_model(Article)
        sidenew_type = ContentType.objects.get_for_model(SideNew)
        results = {"articles":[],
                   "sidenews":[],
                   "user":user,
                   "logout_url":settings.LOGOUT_URL,
                   "form":CommentForm()}

        for entry in articles:
            article_serializer = ArticleSerializer(entry)
            ct = entry.model_content_type
            pk = entry.pk
            comments = Comment.objects.filter(content_type=ct, object_id=pk)
            cmts = []
            for cmt in comments:
                cmt_serializer = CommentSerializer(cmt)
                cmts.append( cmt_serializer.data )
            art_cmt = { "art":article_serializer.data,
                        "cmts":cmts,
                        "model_content_type": article_type.id}
            results["articles"].append( art_cmt )


        for entry in sidenews:
            sdn_serializer = SideNewSerializer(entry)
            ct = entry.model_content_type
            pk = entry.pk
            comments = Comment.objects.filter(content_type=ct, object_id=pk)
            cmts = []
            for cmt in comments:
                cmt_serializer = CommentSerializer(cmt)
                cmts.append( cmt_serializer.data )
            sdn_cmt = {"art":sdn_serializer.data,
                        "cmts":cmts,
                        "model_content_type": sidenew_type.id}
            results["sidenews"].append( sdn_cmt )


        # entries = list(chain(articles, sidenews)) # combine the two querysets
        # for entry in entries:
        #     if isinstance(entry, Article):
        #         print type(Article)
        #         serializer = ArticleSerializer(entry)
        #         results["articles"]["articles"].append( serializer.data )
        #     if isinstance(entry, SideNew):
        #         serializer = SideNewSerializer(entry)
        #         results["sidenews"]["sidenews"].append( serializer.data )

        # print results

        return Response(results,template_name='bobthings.html')


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


from django.views.generic import View, TemplateView, ListView
from django.utils.decorators import method_decorator

class BobthingsView(ListView):

    template_name = 'bobthings.html'
    context_object_name = 'results'

    def get_context_data(self, **kwargs):

        context = super(BobthingsView, self).get_context_data(**kwargs)
        context.update({'items_per_page':self.paginate_by})
        return context

    def get_queryset(self):
        articles = Article.objects.all()
        articles.order_by('created')
        sidenews = SideNew.objects.all()
        sidenews.order_by('created')

        query= {"articles": articles,
                "sidenews": sidenews}

        return query

    def get_paginate_by(self, queryset):

        self.paginate_by = self.request.GET.get('limit', 20)
        return self.paginate_by

    @method_decorator(never_cache)
    def get(self, request, *args, **kwargs):
        return super(BobthingsView, self).get(request, *args, **kwargs)



# class Comment(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Comment.objects.get(pk=pk)
#         except Comment.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         comment = self.get_object(pk)
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#
#         data=request.DATA
#
#         if request.user.is_authenticated():
#             data["created_by"] = request.user.id
#             data["updated_by"] = request.user.id
#         else:
#             return Response("require authentication", status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = CommentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             #bobthings_comment.content_type_id may not be NULL
#             print serializer.data
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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