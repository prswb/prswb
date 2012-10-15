# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from generic import views as generic_views
from pages import views as pages_views
from websites import views as websites_views


admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^$', pages_views.dashboard, name='homepage'),
    url(r'^i18n/(?P<lang>[a-z]{2,})/$', generic_views.change_language,
        name='change_language'),

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

    # registration, accounts
    url(r'^compte/', include('registration.backends.default.urls')),
)

# non i18 urls
urlpatterns += patterns('',
    # pages
    url(r'^pages/(?P<slug>[-\w\d]+)/$', 'pages.views.markdown_page',
        name='markdown_page'),
    url(r'^imagefit/', include('imagefit.urls')),
    )

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
               'document_root': settings.STATIC_ROOT,
           }),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
               'document_root': settings.MEDIA_ROOT,
           }),
    )
