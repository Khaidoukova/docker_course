from datetime import datetime, timedelta
import requests
from celery import shared_task
from tracker.models import Habit
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
        reminder_date = habit.next_reminder_date
        reminder_time = habit.time
        chat_id = habit.user.chat_id
        print(reminder_time, reminder_date)

        if reminder_date <= now_date or reminder_time is None:
            if reminder_time <= now_time:
                # tg_send_message(chat_id, f'Напоминание: нужно {action} в {location} в {reminder_time}')
                url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
                text = f'Напоминание: нужно {action} в {location} в {reminder_time}'
                params = {'chat_id': chat_id, 'text': text}
                response = requests.get(url, params=params)
                print(f'Сообщение отправлено: {response.json()}')

            habit.next_reminder_date = now_date + timedelta(days=frequency)
            habit.save()
