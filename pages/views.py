# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mass_mail
from pages.forms import ContactForm
from django.conf import settings

@csrf_protect
def contact(request):
    """ Contact form
    Display and proceed contact form submission
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data)
            return HttpResponseRedirect('/contact/merci')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})

def confirm_contact(request):
    """ Contact form confirmation """
    return render(request, 'pages/confirm_contact.html')

def send_message(data):
    to_sender_message = """
Bonjour,

Votre commentaire sur le site www.uxperiment.fr a bien été pris en compte.

Nous vous remercions de votre participation.

A bientôt,

L'équipe UXperiment
"""
    to_admin_message = 'Emetteur : %s \n %s' % (data['sender'], data['message'])
    to_sender = ('Commentaire sur UXperiment', to_sender_message, 
            'no-reply@uxperiment.fr', [data['sender']])
    to_admin = (data['subject'], to_admin_message, data['sender'], 
        [settings.EMAIL_RECIPIENT])
    send_mass_mail((to_sender, to_admin))
