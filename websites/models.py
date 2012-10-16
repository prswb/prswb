# -*- coding: utf-8 -*-

import hashlib
import os

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


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
