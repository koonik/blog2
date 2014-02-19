from django.conf.urls import patterns, url
from post import views
from post.models import Post
from author.models import User

urlpatterns = patterns('',
    url('^$', views.index, name='index'),
)

urlpatterns += patterns('',
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
)
