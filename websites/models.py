# -*- coding: utf-8 -*-

import hashlib
import os
import re
import requests

from django.db import models
from django.forms import URLField
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from bs4 import BeautifulSoup


def website_upload_to(instance, filename):
    return os.path.join("websites", "%s.jpg" % hashlib.sha1(instance.url).hexdigest())


class Website(models.Model):

    REQUEST_COMMENT = 'comment'
    REQUEST_IMPROVE = 'improve'
    REQUEST_DEBUG = 'debug'

    REQUEST_CHOICES = (
        (REQUEST_COMMENT, _(u"Comment")),
        (REQUEST_IMPROVE, _(u"Enhancement suggestion")),
        (REQUEST_DEBUG, _(u"Problem or bug")),
    )

    submitter = models.ForeignKey(User, null=True)
    url = models.URLField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    picture = models.ImageField(upload_to=website_upload_to, null=True, blank=True)
    request_type = models.CharField(max_length=30, choices=REQUEST_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ('-date',)

#----------------------------


def get_url_informations(url):
    """Get informations about a url"""

    error_invalid = False, {'error': _(u'Invalid URL')}
    error_exist = False, {'error': _(u'This URL has already been submitted')}
    error_connect = False, {'error': _(u'Failed at opening the URL')}

    # Check url is valid
    try:
        url_field = URLField()
        clean_url = url_field.clean(url)
    except:
        return error_invalid

    # Check url exist
    if exist_url(clean_url):
        return error_exist

    # Get informations
    req = requests.get(clean_url)
    if 200 == req.status_code:
        final_url = req.url
        soup = BeautifulSoup(req.text)
        title = soup.title.string
        description = soup.findAll('meta',
                                   attrs={'name': re.compile("^description$", re.I)})[0].get('content')
    else:
        return error_connect

    # Check final url exist if different from clean url
    if final_url != clean_url:
        if exist_url(final_url):
            return error_exist

    return True, {
        'url': final_url,
        'title': title,
        'description': description,
    }


def exist_url(url):
    """Check url exist"""
    return Website.objects.filter(url__exact=url).exists()
