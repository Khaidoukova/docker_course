from datetime import datetime

from django.db import models
from django.utils import timezone

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, )
    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='Место')
    time = models.TimeField(default=timezone.now, null=True, blank=True, verbose_name='Время')
    action = models.CharField(max_length=200, null=True, blank=True, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, null=True, blank=True, verbose_name='Признак приятной привычки')
    connected_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name='Связанная привычка')
    frequency = models.IntegerField(default=1, null=True, blank=True, verbose_name='Периодичность в днях')
    reward = models.CharField(max_length=200, null=True, blank=True, verbose_name='Вознаграждение')
    duration = models.IntegerField(default=5, null=True, blank=True, verbose_name='Время на выполнение в минутах')
    public = models.BooleanField(default=False, null=True, blank=True, verbose_name='Признак публичности')
    last_reminder_date = models.DateField(default=timezone.now, verbose_name='дата последнего напоминания')

    def __str__(self):
        return f'я буду {self.action} в {self.time} в {self.location}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'







