from django.db import models
from django.template.defaultfilters import slugify
from django import forms
from ckeditor.widgets import CKEditorWidget


class Post(models.Model):
    title = models.CharField(max_length=250)
    post_content = models.CharField(max_length=6000)
    pub_date = models.DateTimeField('published')
    year = models.IntegerField()
    month = models.IntegerField()
    slug = models.SlugField()

    def get_year(self):
        year = self.pub_date.year
        return year
    year = property(get_year)

    def get_month(self):
        month = self.pub_date.month
        return month
    month = property(get_month)

    def get_slug(self):
        slug = slugify(self.title)
        return slug
    slug = property(get_slug)

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.year, self.month, self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]


class PostForm(forms.ModelForm):
        content = forms.CharField(widget=CKEditorWidget())
        class Meta:
            model = Post
            fields = ['title', 'post_content', 'pub_date']

