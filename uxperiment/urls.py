# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from generic import views as generic_views
from pages import views as pages_views
from websites import views as websites_views
from registration.backends.default import urls as registration_urls
from django import views as django_views
from imagefit import urls as imagefit_urls

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^$', pages_views.dashboard,
        name='homepage'),
    url(r'^i18n/(?P<lang>[a-z]{2,})/$', generic_views.change_language,
        name='change_language'),

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # contact
    url(r'^contact/$', pages_views.contact,
        name='contact'),
    url(r'^contact/merci/$', pages_views.confirm_contact,
        name='confirm_contact'),

    # website
    url(r'^sites-proposes/$', websites_views.index,
        name='websites_index'),
    url(r'^proposer-un-site/$', websites_views.suggest,
        name='suggest_website'),
    url(r'^proposer-un-site/merci/$', websites_views.confirm_suggest,
        name='confirm_suggest_website'),
    url(r'^informations-sur-un-site/$', websites_views.informations,
        name='informations_website'),

    # registration, accounts
    url(r'^compte/', include(registration_urls)),
)

# non i18 urls
urlpatterns += patterns('',
    # pages
    url(r'^pages/(?P<slug>[-\w\d]+)/$', pages_views.markdown_page,
        name='markdown_page'),

    # imagefit
    url(r'^imagefit/', include(imagefit_urls)),

    # static files
    url(r'^static/(?P<path>.*)$', django_views.static.serve, {
           'document_root': settings.STATIC_ROOT,
       }),

    # media files
    url(r'^media/(?P<path>.*)$', django_views.static.serve, {
           'document_root': settings.MEDIA_ROOT,
       }),
)
