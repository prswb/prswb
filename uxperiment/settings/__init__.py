import os
import importlib

try:
    importlib.import_module(os.environ.get('UXPERIMENT_ENV', 'production'))
except ImportError:
    from .base import *

# local settings
try:
    from .local import *
except ImportError:
    pass
