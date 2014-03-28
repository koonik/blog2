from django.conf.urls import patterns, include, url
from rest_framework import routers
from blog import views

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = router.urls


urlpatterns += patterns('',
    url(r'^', include('blog.urls')),
    url(r'^', include('comments.urls')),
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),

)

