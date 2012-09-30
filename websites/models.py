# -*- coding: utf-8 -*-
import re
import requests
from django.db import models
from django.forms import URLField
from bs4 import BeautifulSoup

class Website(models.Model):
    url         = models.URLField(max_length=255, unique=True)
    title       = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    picture     = models.CharField(max_length=255)



def get_url_informations(url):
    """Get informations about a url"""

    error_invalid = False, { 'error': u'Url invalide' }
    error_exist   = False, { 'error': u'Cette url existe déjà' }
    error_connect = False, { 'error': u'Impossible de se connecter au site' }

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
        final_url   = req.url
        soup        = BeautifulSoup(req.text)
        title       = soup.title.string
        description = soup.findAll('meta',
            attrs={'name':re.compile("^description$", re.I)})[0].get('content')
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
