from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from product.models import Items
from product import views


urlpatterns = patterns('',
        url(r'^Home/$', views.home, name='home'),
        url(r'^new_item/$', views.new_item, name='new_item'),
        url(r'^(?P<i_id>\d+)/$', views.edit_item, name='edit_item'),
        url(r'^all_items/$', views.all, name='all_items'),		
)