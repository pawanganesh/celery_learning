from celery import shared_task

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    # timezone.localtime(users.last_login) + timedelta(days=1)
    for user in users:
        send_mail(
            subject='Test',
            message='Test',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email, ],
            fail_silently=False,
        )
    return 'Done'
