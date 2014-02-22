from django.conf.urls import patterns, url
from post import views


urlpatterns = patterns('',
    url('^$', views.index, name='index'),
    url('^blog/$', views.blog_view, name='blog_view'),
    url('^blog/(?P<id>\d+)/$', views.post_edit, name="post_edit"),
    url('^blog/add_post/$', views.add_post, name="add_post"),
)

urlpatterns += patterns('',
    url(r'^month/(\d+)/(\d+)/$', views.month),

)

urlpatterns += patterns('',
    url(r'^(\d{4})/(\d{1,2})/(?P<id>\d+)/$', views.detail, name='detail'),
)

urlpatterns += patterns('',
    url('^login/$', views.log_in_page, name='login_page'),
    url('^login/login/$', views.log_in, name='login'),
)

urlpatterns += patterns('',
    url('^logout/$', views.log_out, name='logout'),

)
