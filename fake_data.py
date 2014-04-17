from bobthings.models import News
from bobthings.serializer import NewsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

new = News(title = "test 1", article='something')
new.save()

new = News(title = "test 2", article='something else')
new.save()

# serializer = NewsSerializer(snippet)
# serializer.data