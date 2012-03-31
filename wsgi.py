import os
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_DIR, '..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'maitreya_van.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
