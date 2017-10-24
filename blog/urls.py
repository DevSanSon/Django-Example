from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_blog, name="all_blog"),
    url(r'^(?P<id>[-\w]+)/$', views.post_detail, name="post_detail"),
]
