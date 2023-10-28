from datetime import datetime, timedelta

from celery import shared_task
from tracker.models import Habit
from tracker.utils import tg_send_message


@shared_task
def habits_to_telegram(**kwargs):
    habits = Habit.objects.filter(is_pleasant=False)
    now = datetime.now()
    for habit in habits:
        last_reminder = habit.last_reminder_date
        period = habit.frequency
        next_reminder = last_reminder + timedelta(days=period)
        if now >= next_reminder:
            habit.last_reminder_date = next_reminder
            tg_send_message(habit.user.chat_id, str(habit))
            habit.save()










