# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uxperiment.views.home', name='home'),
    # url(r'^uxperiment/', include('uxperiment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pages.views.dashboard', name='dashboard'),
    url(r'^contact/$', 'pages.views.contact', name='contact'),
    url(r'^contact/merci/$', 'pages.views.confirm_contact',
        name='confirm_contact'),

    # Suggest a website
    url(r'^proposer-un-site/$', 'websites.views.suggest',
        name='suggest_website'),
    url(r'^proposer-un-site/merci/$', 'websites.views.confirm_suggest',
        name='confirm_suggest_website'),
    url(r'^informations-sur-un-site/$', 'websites.views.informations',
        name='informations_website'),

    url(r'^pages/(?P<slug>[-\w\d]+)/$', 'pages.views.markdown_page',
        name='markdown_page'),
    url(r'^compte/', include('registration.urls')),
)

# local dev

urlpatterns += patterns('',
     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
