import os
import dj_database_url

from .base import *


INSTALLED_APPS += (
    'gunicorn',
)

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

EMAIL_RECIPIENT = os.environ.get('EMAIL_RECIPIENT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
