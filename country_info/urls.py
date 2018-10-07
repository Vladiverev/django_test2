from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.country_list, name='country_list'),
    url(r'^c_city/(?P<pk>[\w-]+)/$', views.c_city, name='c_city'),
    url(r'^city_add/(?P<pk>[\w-]+)/$', views.city_add, name='city_add'),
    url(r'^city_edit/(?P<pk_count>[\w-]+)/(?P<pk_city>[\w-]+)/$', views.city_edit, name='city_edit'),
    url(r'^c_city/(?P<pk_count>[\w-]+)/(?P<pk_city>[\w-]+)/remove/$', views.city_remove, name='city_remove'),
]