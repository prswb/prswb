# coding: utf-8
from django.core.mail import send_mass_mail
from django.conf import settings

message = {
    "contact": '''\
Bonjour,

Votre commentaire sur le site www.uxperiment.fr a bien été pris en compte.

Nous vous remercions de votre participation.

A bientôt,

L'équipe UXperiment
''',
    "suggest": '''\
Bonjour,

Votre proposition de site internet sur le site www.uxperiment.fr a bien été pris en compte.

Nous vous remercions de votre participation.

A bientôt,

L'équipe UXperiment
''',
}

def send_message(confirm, data):
    send_mass_mail((build_user_email(confirm, data['sender']), 
        build_admin_email(confirm, data)))

def build_user_email(confirm, recipient):
    """ Build user message in form of send_mail """
    text = message[confirm]
    if confirm == 'suggest':
        subject = 'Confirmation de votre proposition sur UXperiment'
    if confirm == 'contact':
        subject = 'Commentaire sur UXperiment'
    if confirm == 'signin':
        subject = 'Confirmation d\'inscription sur UXperiment'

    return subject, text, settings.EMAIL_HOST_USER, [recipient]

def build_admin_email(confirm, data):
    """ Build admin message in form of send_mail """
    if confirm == 'suggest':
        subject = 'Nouvelle proposition de site sur UXperiment'
        text = 'L\'utilisateur : %s, vient de proposer le site %s'\
        % (data['username'], data['website'])

    if confirm == 'contact':
        subject = 'Nouveau contact sur UXperiment'
        text = '''\
Email : %s
Sujet : %s
Message :
%s''' % (data['sender'], data['subject'], data['message'])

    return subject, text, settings.EMAIL_HOST_USER, [settings.EMAIL_RECIPIENT]
