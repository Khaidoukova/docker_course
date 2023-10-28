from datetime import timedelta

from rest_framework.exceptions import ValidationError


class ConnectedHabitOrRewardValidator:

    def __init__(self, connected_habit, reward):
        self.connected_habit = connected_habit
        self.reward_field = reward

    def __call__(self, values):
        connected_habit = values.get(self.connected_habit)
        reward = values.get(self.reward)
        if connected_habit and reward:
            raise ValidationError('Выберите приятную привычку ИЛИ вознаграждение')


class TimeLimitValidator:

    def __init__(self, duration):
        self.duration = duration

    def __call__(self, value):
        duration = value.get(self.duration)
        if duration > timedelta(seconds=120):
            raise ValidationError('Длительность выполнения не может превышать 120 секунд!')


class FrequencyValidation:

    def __init__(self, frequency):
        self.frequency = frequency

    def __call__(self, value):
        frequency = value.get(self.frequency)
        if frequency > 7:
            raise ValidationError('Привычка должна выполняться НЕ реже 1 раза в неделю')