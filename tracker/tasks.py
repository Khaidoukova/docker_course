from datetime import datetime, timedelta
import logging
from celery import shared_task
from tracker.models import Habit
from tracker.utils import tg_send_message


@shared_task
def habits_to_telegram():
    now_hour = datetime.now().hour
    now_min = datetime.now().minute
    habits = Habit.objects.filter(
        time__hour=now_hour,
        time__minute=now_min
    )
    for habit in habits:
        action = habit.action
        location = habit.location
        time = habit.time
        chat_id = habit.user.chat_id

        tg_send_message(chat_id, f'Напоминание: нужно {action} в {location} в {time}')
















