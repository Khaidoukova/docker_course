import requests
from django.conf import settings
import json
from datetime import datetime, date, timedelta
from django_celery_beat.models import PeriodicTask, IntervalSchedule

def tg_get_updates():
    response = requests.get(f'https://api.telegram.org/bot{settings.Telegram_bot_API}/getUpdates')
    return response.json()


def tg_send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    requests.get(f'https://api.telegram.org/bot{settings.Telegram_bot_API}/sendMessage', params=params)
    return


def set_schedule(frequency, pk, time):

    schedule, created = IntervalSchedule.objects.get_or_create(
         every=frequency,
         period=IntervalSchedule.DAYS,
     )
    return PeriodicTask.objects.create(
        interval=schedule,
        name=f'{pk}',
        task='tracker.tasks.habits_to_telegram',
        start_time=datetime.combine(date.today(), time),
        args=json.dumps({}),
        kwargs=json.dumps({'pk': pk})
    )