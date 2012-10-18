# coding: utf-8
from django.core.mail import send_mass_mail
from django.conf import settings
from django.template.loader import get_template
from django.utils.translation import get_language, ugettext as _


from django.template import Context


def send_message(confirm, data):
    send_mass_mail((build_user_email(confirm, data['sender']),
        build_admin_email(confirm, data)))


def build_user_email(confirm, recipient):
    """ Build user message in form of send_mail """
    subjects = (
        ('suggest', _("Confirmation de votre proposition sur UXperiment")),
        ('contact', _("Commentaire sur UXperiment")),
        ('signin', _("Confirmation d'inscription sur UXperiment")),
        )
    subject = dict(subjects).get(confirm)
    lang = get_language()[0:2]
    message = get_template('mails/%s/%s.txt' % (lang, confirm))\
                .render(Context())

    return subject, message, settings.EMAIL_HOST_USER, [recipient]


def build_admin_email(confirm, data):
    """ Build admin message in form of send_mail """
    subjects = (
        ('suggest', _("Nouvelle proposition de site sur UXperiment")),
        ('contact', _("Nouveau contact sur UXperiment")),
        )
    subject = dict(subjects).get(confirm)
    message = get_template('mails/admin_%s.txt' % confirm).render(Context(dict(
        data=data
        )))
    return subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_RECIPIENT]
