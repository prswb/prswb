from django.core.mail import send_mass_mail
from django.conf.settings import EMAIL_RECIPIENT, EMAIL_HOST_USER

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

def send_message(website, username, email):
    subject = '    to_sender_message = 
    to_admin_message = 'L''utilisateur : %s, vient de proposer le site %s'\
        % (username, website)
    to_sender = (subject, to_sender_message, 'no-reply@uxperiment.fr',
            [email])
    to_admin = (subject, to_admin_message, email,
        [settings.EMAIL_RECIPIENT])
    send_mass_mail((to_sender, to_admin))
    
def send_message(data,confirm):
    to_sender_message = message[confirm]
    to_admin_message = '    to_sender = (', to_sender_message[confirm],
            'no-reply@uxperiment.fr', [data['sender']])
    to_admin = (data['subject'], to_admin_message, data['sender'],
        [settings.EMAIL_RECIPIENT])
    send_mass_mail((build_user_email(confirm, data[, to_admin))

def build_user_email(confirm, recipient)
    """ Build user message in form of send_mail """
    text = message[confirm]
    if confirm == 'suggest':
        subject = 'Confirmation de votre proposition sur UXperiment'
    if confirm == 'contact':
        subject = 'Commentaire sur UXperiment'
    if confirm = 'signin':
        subject = 'Confirmation d\'inscription sur UXperiment'
    
    return (subject, text, EMAIL_HOST_USER, [recipient])

def build_admin_email(confirm, data):
    """ Build admin message in form of send_mail """
    if confirm == 'suggest':
        subject = 'Nouvelle proposition de site sur UXperiment'
        text = 'L\'utilisateur : %s, vient de proposer le site %s'\
        % (data['username'], data['website'])

    if confirm == 'contact':
        subject = 'Nouveau contact sur UXperiment'
        text = '''\
Adresse email : %s

---------------------------------------
%s''' % (data['sender'], data['message'])

    return (subject, text, EMAIL_HOST_USER, [EMAIL_RECIPIENT])



