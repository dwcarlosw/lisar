from django.forms import widgets
from rest_framework import serializers



from django.forms import widgets
from rest_framework import serializers
from bobthings.models import Article, SideNew
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    created_by = serializers.Field(source='created_by.username')

    class Meta:
        model = Article
        fields = ('id', 'title', 'article', 'created_by')

class SideNewSerializer(serializers.ModelSerializer):
    created_by = serializers.Field(source='created_by.username')

    class Meta:
        model = SideNew
        fields = ('id', 'title', 'article', 'created_by')

class UserSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'news')


# class NewsSerializer(serializers.Serializer):
#
#     pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
#     title = serializers.CharField(required=False,
#                                   max_length=100)
#     article = serializers.CharField(widget=widgets.Textarea,
#                                  max_length=100000)
#
#     def restore_object(self, attrs, instance=None):
#         """
#         Create or update a new snippet instance, given a dictionary
#         of deserialized field values.
#
#         Note that if we don't define this method, then deserializing
#         data will simply return a dictionary of items.
#         """
#         if instance:
#             # Update existing instance
#             instance.title = attrs.get('title', instance.title)
#             instance.article = attrs.get('code', instance.code)
#             return instance
#
#         # Create new instance
#         return News(**attrs)