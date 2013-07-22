__author__ = 'Swan'

from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SmplBB.views.home', name='home'),
    # url(r'^SmplBB/', include('SmplBB.foo.urls')),

    url(r'^$', views.index, name='home'),

    url(r'^(?P<topic_id>\d+)/$', views.topic, name='topic'),

    url(r'^(?P<topic_id>\d+)/reply/$', views.reply, name='reply'),

    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    url(r'^new_topic/post/$', views.new_topic_create, name='new_topic_create'),
)
