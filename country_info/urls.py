from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.country_list, name='country_list'),
]