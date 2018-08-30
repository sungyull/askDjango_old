from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/$', views.myname),
    url(r'^hello/(?P<name>[a-zA-Zㄱ-힣]+)/(?P<age>[\d]+)/$', views.myname),
]
