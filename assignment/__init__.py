import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')

import django
django.setup()

from .celery import app as celery_app

