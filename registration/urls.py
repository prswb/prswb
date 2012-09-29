# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('', 
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^creation/$', 'registration.views.signin', name="signin"),
)
