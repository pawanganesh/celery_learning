from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_proj.settings')

app = Celery('celery_proj')
# app.conf.enable_utc = True
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kathmandu', )

app.config_from_object(settings, namespace='CELERY')

# Celery beat settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'send_mail_app.tasks.send_mail_func',
        # 'schedule': crontab(hour=17, minute=52, day_of_month=19, month_of_year=6), # single execution
        'schedule': crontab(hour=17, minute=52),
        # 'args': (1, 2)
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
