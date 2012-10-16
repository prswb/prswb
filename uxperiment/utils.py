# coding: utf-8
from django.core.mail import send_mass_mail
from django.conf import settings
from django.template.loader import get_template

from django.template import Context


def send_message(confirm, data):
    send_mass_mail((build_user_email(confirm, data['sender']),
        build_admin_email(confirm, data)))

def build_user_email(confirm, recipient):
    """ Build user message in form of send_mail """
    subjects = (
        ('suggest', "Confirmation de votre proposition sur UXperiment"),
        ('contact', "Commentaire sur UXperiment"),
        ('signin', "Confirmation d'inscription sur UXperiment"),
        )
    subject = dict(subjects).get(confirm)
    message = get_template('mails/%s.txt' % confirm).render(Context())

    return subject, message, settings.EMAIL_HOST_USER, [recipient]

def build_admin_email(confirm, data):
    """ Build admin message in form of send_mail """
    if confirm == 'suggest':
        subject = 'Nouvelle proposition de site sur UXperiment'
        text = 'L\'utilisateur : %s, vient de proposer le site %s'\
        % (data['username'], data['website'])

    elif confirm == 'contact':
        subject = 'Nouveau contact sur UXperiment'
        text = '''\
Email : %s
Sujet : %s
Message :
%s''' % (data['sender'], data['subject'], data['message'])

    return subject, text, settings.EMAIL_HOST_USER, [settings.EMAIL_RECIPIENT]
