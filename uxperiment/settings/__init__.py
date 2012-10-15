import os

UXPERIMENT_ENV = os.environ.get('UXPERIMENT_ENV')

if UXPERIMENT_ENV == 'dev':
    from .dev import *
elif UXPERIMENT_ENV == 'test':
    from .test import *
elif UXPERIMENT_ENV == 'staging':
    from .staging import *
elif UXPERIMENT_ENV == 'production':
    from .production import *
else:
    from .base import *

# local settings
try:
    from .local import *
except ImportError:
    pass
