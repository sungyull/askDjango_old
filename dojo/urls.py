from django.conf.urls import url
from . import views
from . import views_cbv


urlpatterns = [
    url(r'^new/$', views.post_new),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit),

    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/$', views.myname),
    url(r'^hello/(?P<name>[a-zA-Zㄱ-힣]+)/(?P<age>[\d]+)/$', views.myname),

    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^xls/$', views.excel_down),

    url(r'^cbv/list1/$', views_cbv.post_list1),
    url(r'^cbv/list2/$', views_cbv.post_list2),
    url(r'^cbv/list3/$', views_cbv.post_list3),
    url(r'^cbv/xls/$', views_cbv.post_list4),
]
