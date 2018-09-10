from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    # path('<int:id>/', views.post_detail, name='post_detail'),
]

