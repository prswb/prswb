# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings

# views and urls imports
from pages import views as pages_views
from websites import views as websites_views
from registration import urls as registration_urls
from django import views as django_views


urlpatterns = patterns('',
    url(r'^$', pages_views.dashboard, name='dashboard'),
    url(r'^contact/$', pages_views.contact, name='contact'),
    url(r'^contact/merci/$', pages_views.confirm_contact,
        name='confirm_contact'),

    # Suggest a website
    url(r'^proposer-un-site/$', websites_views.suggest,
        name='suggest_website'),
    url(r'^proposer-un-site/merci/$', websites_views.confirm_suggest,
        name='confirm_suggest_website'),
    url(r'^informations-sur-un-site/$', websites_views.informations,
        name='informations_website'),

    url(r'^pages/(?P<slug>[-\w\d]+)/$', pages_views.markdown_page,
        name='markdown_page'),
    url(r'^compte/', include(registration_urls)),
)


# local dev
urlpatterns += patterns('',
     url(r'^static/(?P<path>.*)$', django_views.static.serve, {
            'document_root': settings.STATIC_ROOT,
        }),
     url(r'^media/(?P<path>.*)$', django_views.static.serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
)
