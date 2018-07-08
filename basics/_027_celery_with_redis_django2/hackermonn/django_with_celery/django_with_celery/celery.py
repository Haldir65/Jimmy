# django_with_celery/celery.py
from __future__ import absolute_import
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_with_celery.settings') # DON'T FORGET TO CHANGE THIS ACCORDINGLY
app = Celery('django_with_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
