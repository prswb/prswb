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


def index(request):
    return render(request, 'websites/index.html', {
        'websites': Website.objects.all(),
    })


@login_required
def suggest(request):
    """
    Suggest form
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
        return redirect('confirm_suggest_website')

    return render(request, 'websites/suggest.html', {'form': form})


def confirm_suggest(request):
    """ Suggest form confirmation """
    return render(request, 'websites/confirm_suggest.html')


def informations(request):
    """ Get informations about a website """
    if request.is_ajax():
        success = False
        status = 400
        infos = {'error': _(u'Invalid request')}
        url = request.GET.get('url', False)
        if url:
            success, infos = get_url_informations(url)

            if success:
                status = 200
            else:
                status = 409

        return HttpResponse(json.dumps(infos),
            content_type="application/json", status=status)
    else:
        raise Http404("This view should be called in ajax")
