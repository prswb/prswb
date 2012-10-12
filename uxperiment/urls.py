# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

from pages import views as pages_views
from websites import views as websites_views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', pages_views.dashboard, name='homepage'),
    url(r'^sites-proposes/$', websites_views.list, name='websites_list'),

    url(r'^admin/', include(admin.site.urls)),

    # contact
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

    # pages
    url(r'^pages/(?P<slug>[-\w\d]+)/$', 'pages.views.markdown_page',
        name='markdown_page'),

    # registration, accounts
    url(r'^compte/', include('registration.backends.default.urls')),
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
