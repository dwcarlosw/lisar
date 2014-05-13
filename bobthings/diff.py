from reversion.helpers import generate_patch_html
import reversion
from bobthings.models import Article
articles = Article.objects.all()[0]

available_version = reversion.get_for_object(articles)
print available_version
old_version = available_version[0]
new_version = available_version[1]

patch_html = generate_patch_html(old_version, new_version, "article")
print patch_html