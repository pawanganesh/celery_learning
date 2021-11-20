from django.urls import path

from .views import test, send_mail_to_all, schedule_mail

app_name = 'mainapp'
urlpatterns = [
    path('', test, name='test'),
    path('sendmail/', send_mail_to_all, name='send-mail-to-all'),
    path('schedulemail/', schedule_mail, name='schedule-mail'),
]