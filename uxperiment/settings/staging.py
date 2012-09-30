from uxperiment.settings.base import *
import dj_database_url
import os

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

INSTALLED_APPS += (
    'gunicorn',
)

EMAIL_RECIPIENT = os.environ['EMAIL_RECIPIENT']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
