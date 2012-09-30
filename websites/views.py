# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse
from django.core.mail import send_mass_mail
from django.conf import settings
from websites.models import get_url_informations
from websites.forms import SuggestForm

@csrf_protect
def suggest(request):
    """ Suggest form
    Display and proceed suggest a website form submission
    """
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            website = form.save()
            send_message(
                website.url,
                'TODO authenticated username',
                settings.EMAIL_RECIPIENT # Replace with user email
            )
            return HttpResponseRedirect(reverse('confirm_suggest_website'))
    else:
        form = SuggestForm()
    return render(request, 'websites/suggest.html', {'form': form})

def confirm_suggest(request):
    """ Suggest form confirmation """
    return render(request, 'websites/confirm_suggest.html')

def informations(request):
    """ Get informations about a website """
    if request.is_ajax():
        success = False
        infos = { 'error': u'Requête invalide' }
        if 'GET' == request.method:
            success, infos = get_url_informations(request.GET['url'])

            if success:
                status=200
            else:
                status=409

        return HttpResponse(json.dumps(infos),
            content_type="application/json", status=status)
    else:
        raise Http404

def send_message(website, username, email):
    subject = 'Proposition de site internet sur UXperiment'
    to_sender_message = """
Bonjour,

Votre proposition de site internet sur le site www.uxperiment.fr a bien été pris en compte.

Nous vous remercions de votre participation.

A bientôt,

L'équipe UXperiment
"""
    to_admin_message = 'L''utilisateur : %s, vient de proposer le site %s'\
        % (username, website)
    to_sender = (subject, to_sender_message, 'no-reply@uxperiment.fr',
            [email])
    to_admin = (subject, to_admin_message, email,
        [settings.EMAIL_RECIPIENT])
    send_mass_mail((to_sender, to_admin))
