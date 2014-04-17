from django.db import models

class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    article = models.TextField()
    created_by = models.ForeignKey('auth.User', blank=True, null=True, related_name='%(app_label)s_%(class)s_created')
    updated_by = models.ForeignKey('auth.User', blank=True, null=True, related_name='%(app_label)s_%(class)s_updated')

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)


class SideNew(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    article = models.TextField()
    created_by = models.ForeignKey('auth.User', blank=True, null=True, related_name='%(app_label)s_%(class)s_created')
    updated_by = models.ForeignKey('auth.User', blank=True, null=True, related_name='%(app_label)s_%(class)s_updated')

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(SideNew, self).save(*args, **kwargs)