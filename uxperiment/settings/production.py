import os

from .base import *


DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'USER':     os.environ.get('UXPERIMENT_POSTGRES_USERNAME', 'postgres'),
        'PASSWORD': os.environ.get('UXPERIMENT_POSTGRES_PASSWORD'),
        'HOST':     os.environ.get('UXPERIMENT_POSTGRES_HOST', 'localhost'),
        'PORT':     os.environ.get('UXPERIMENT_POSTGRES_PORT', 5432),
    }
}

EMAIL_RECIPIENT = os.environ.get('EMAIL_RECIPIENT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
