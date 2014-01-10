# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import ListView
from twatter.models import Twat
from twatter.views import PostTwat, ListTwats

urlpatterns = patterns('',
    url(r'^$', ListTwats.as_view(), name='list_twats'),
    url(r'^post/$', PostTwat.as_view(), name='post_twat'),
    url(r'^last/$', 'twatter.views.last'),
)
