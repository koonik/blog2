from django.conf.urls import patterns, url
from comments import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^comments$', views.CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)$', views.CommentDetail.as_view()),
)

