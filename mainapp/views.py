import json
from django.http import HttpResponse

from django_celery_beat.models import PeriodicTask, CrontabSchedule

from .tasks import test_func
from send_mail_app.tasks import send_mail_func


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Mail Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=21, minute=41, day_of_week='*')
    task = PeriodicTask.objects.create(crontab=schedule, name='schedule_mail_task_' + '1',
                                       task='send_mail_app.tasks.send_mail_func', )  # args=json.dumps([[2, 3]]))
    return HttpResponse("Mail Scheduled")
