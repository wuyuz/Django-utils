from django.conf.urls import url
from rbac import views

urlpatterns = [

    url(r'^role/list/$', views.role_list, name='role_list'),
    url(r'^role/add/$', views.role_change, name='role_add'),
    url(r'^role/edit/(\d+)/$', views.role_change, name='role_edit'),

    url(r'^menu/list/$', views.menu_list, name='menu_list'),
    url(r'^menu/add/$', views.menu_change, name='menu_add'),
    url(r'^menu/edit/(\d+)/$', views.menu_change, name='menu_edit'),

]