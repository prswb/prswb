# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('', 
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^creation/$', 'registration.views.signin', name="signin"),
    url(r'^creation/merci$', 'registration.views.confirm_signin', 
        name="confirm_signin"),
)
