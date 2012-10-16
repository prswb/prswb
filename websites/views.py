# -*- coding: utf-8 -*-

import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

from websites.utils import get_url_informations
from websites.forms import SuggestForm
from models import Website
from uxperiment.utils import send_message


def list(request):
    websites = Website.objects.all()
    return render(request, 'websites/list.html', {
        'websites': websites,
    })


@login_required
def suggest(request):
    """
    Suggest form
    Display and proceed suggest a website form submission
    """
    if request.method == 'POST':
        form = SuggestForm(request.POST, request.FILES)
        if form.is_valid():
            website = form.save(commit=False)
            website.submitter = request.user
            website.save()
            send_message('suggest', {
                'website': website.url,
                'username': request.user.username,
                'sender': request.user.email,
            })
            return redirect('confirm_suggest_website')
    else:
        form = SuggestForm(initial=dict(url='http://'))
    return render(request, 'websites/suggest.html', {
        'form': form,
    })


def confirm_suggest(request):
    """ Suggest form confirmation """
    return render(request, 'websites/confirm_suggest.html')


def informations(request):
    """ Get informations about a website """
    if request.is_ajax():
        success = False
        infos = {'error': _(u'Invalid request')}
        if 'GET' == request.method:
            success, infos = get_url_informations(request.GET['url'])

            if success:
                status = 200
            else:
                status = 409

        return HttpResponse(json.dumps(infos),
            content_type="application/json", status=status)
    else:
        raise Http404("This view should be called in ajax")
