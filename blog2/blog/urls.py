from django.conf.urls import patterns, url
from blog import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^posts$', views.PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)$', views.PostDetail.as_view()),
    url(r'^tags$', views.TagList.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)$', views.TagDetail.as_view()),
    url(r'^blog/$', TemplateView.as_view(template_name='main.html')),
    url('^blog/login/$', views.log_in, name='login'),
    url('^blog/logout/$', views.log_out, name='logout'),
    url(r'^user$', views.CurrentUserView.as_view()),
    url(r'^users$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

