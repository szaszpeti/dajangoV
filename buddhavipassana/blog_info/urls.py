from django.conf.urls import url
from . import views

app_name = 'blog_info'

urlpatterns = [
    #/blog_info
    url(r'^$', views.index, name='blog_index'),
    url(r'^(?P<category_id>[0-9]+)/$', views.details, name='blog_details'),
    url(r'^(?P<category_id>[0-9]+)/$', views.read, name='blog_read')
]