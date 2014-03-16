from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=6000)
    pub_date = models.DateTimeField('date published', auto_now=True)
    tag = models.ManyToManyField(Tag, related_name='tags', related_query_name='tag')
    author = models.ForeignKey('auth.User', related_name='posts')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]


