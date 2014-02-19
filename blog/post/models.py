from django.db import models
from author.models import User


class Post(models.Model):
    title = models.CharField(max_length=250)
    post_content = models.CharField(max_length=6000)
    pub_date = models.DateTimeField('published')
    slug = models.SlugField(max_length=40, unique=True)


    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]

