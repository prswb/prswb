from uxperiment.settings.base import *
import dj_database_url

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

INSTALLED_APPS += (
    'gunicorn',
)
EMAIL_RECIPIENT = 'amanda.martinez@wonderful.fr'
