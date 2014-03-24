from django.db import models
from blog.models import Post


class Comment(models.Model):
    author = models.CharField(max_length=250)
    body = models.CharField(max_length=900)
    pub_date = models.DateTimeField('date published', auto_now=True)
    post = models.ForeignKey(Post, related_name="comments")

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]
