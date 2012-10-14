# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.translation import check_for_language


def change_language(request, lang):
    response = HttpResponseRedirect('/')
    if lang and check_for_language(lang):
        if hasattr(request, 'session'):
            request.session['django_language'] = lang
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response
