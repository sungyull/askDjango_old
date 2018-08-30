from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/$', views.myname),
    url(r'^hello/(?P<name>[a-zA-Zㄱ-힣]+)/(?P<age>[\d]+)/$', views.myname),
    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^xls/$', views.excel_down),
]
