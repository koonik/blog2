from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    post_content = models.TextField(max_length=6000)
    pub_date = models.DateTimeField('date published')


    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]






