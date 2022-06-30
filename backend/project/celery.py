# -*- coding: utf-8 -*-
#author Jack qq:774428957
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
# from django.conf import settings
# from datetime import timedelta
# from celery.schedules import crontab

platforms.C_FORCE_ROOT = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.update(
    CELERYBEAT_SCHEDULE={
    }
)