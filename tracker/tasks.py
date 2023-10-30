from datetime import datetime, timedelta

import requests
from celery import shared_task
from tracker.models import Habit
from tracker.utils import tg_send_message
from django.conf import settings


TOKEN = settings.TG_API


@shared_task
def habits_to_telegram():
    now_time = datetime.now().time()
    now_date = datetime.now().date()

    habits = Habit.objects.filter(is_pleasant=False)
    for habit in habits:
        action = habit.action
        location = habit.location
        frequency = habit.frequency
        reminder_date = habit.last_reminder_date.date() + timedelta(days=frequency)
        reminder_time = habit.time
        chat_id = habit.user.chat_id
        if reminder_date <= now_date:
            if reminder_time == now_time:
                #tg_send_message(chat_id, f'Напоминание: нужно {action} в {location} в {reminder_time}')
                url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
                text = f'Напоминание: нужно {action} в {location} в {reminder_time}'
                params = {'chat_id': chat_id, 'text': text}
                response = requests.get(url, params=params)
                print(f'Сообщение отправлено: {response.json()}')

            habit.last_reminder_date = now_date
            habit.save()

#@shared_task
#@celery_app.on_after_configure.connect
#def habits_to_telegram(sender='tg_send_message', **kwargs):
#    habits = Habit.objects.all()
#    for habit in habits:

#       frequency = habit.frequency
#        chat_id = habit.user.chat_id
#       action = habit.action
#        location = habit.location
#        time = habit.time


#        sender.add_periodic_task(frequency, tg_send_message.d(chat_id, f'Напоминание: нужно {action} в {location} в {time}'), name='habits_to_telegram')

















