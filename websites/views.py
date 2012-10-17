# -*- coding: utf-8 -*-

import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _

from websites.utils import get_url_informations
from websites.forms import SuggestForm
from models import Website
from uxperiment.utils import send_message


def index(request):
    """ Websites index.
    """
    return render(request, 'websites/index.html', {
        'websites': Website.objects.all(),
    })


@login_required
def suggest(request):
    """ Suggest form
        Display and proceed suggest a website form submission
    """
    form = SuggestForm(
        request.POST or None,
        request.FILES or None,
        initial=dict(url='http://')
    )

    if form.is_valid():
        website = form.save(commit=False)
        website.submitter = request.user
        website.save()
        send_message('suggest', {
            'website': website.url,
            'username': request.user.username,
            'sender': request.user.email
        })
        messages.success(request, _('Thanks for your proposition.'))
        return redirect('websites_index')

    return render(request, 'websites/suggest.html', {'form': form})


def informations(request):
    """ Get informations about a website.
    """
    if not request.is_ajax():
        raise Http404("This view should be called in ajax")
    success = False
    status = 400
    infos = {'error': _(u'Invalid request')}
    url = request.GET.get('url', False)
    if url:
        success, infos = get_url_informations(url)
        status = 200 if success else 409
    return HttpResponse(json.dumps(infos),
        content_type="application/json", status=status)
