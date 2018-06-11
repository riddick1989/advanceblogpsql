from django.contrib import admin
from django.urls import path , re_path
from . import views

urlpatterns = [
   path ('/post-create/',views.post_create,name = 'post_create'),
   path ('/post-list/',views.post_list , name= 'post_list'),
   re_path(r'^/(?P<id>\d+)$',views.post_detail, name= 'post-detail'),
   re_path(r'^post-create',views.post_create,name= 'post-create'),
   re_path (r'^/(?P<id>\d+)/edit/$', views.post_update, name='post-update'),
   re_path (r'^/(?P<id>\d+)/delete/$', views.post_delete, name='post-delete'),

]


