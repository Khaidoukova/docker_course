from rest_framework import serializers

from tracker.models import Habit
from tracker.validators import ConnectedHabitOrRewardValidator, TimeLimitValidator, FrequencyValidation


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        #validators = [
        #    ConnectedHabitOrRewardValidator('connected_habit', 'reward'),
        #    TimeLimitValidator('duration'),
        #    FrequencyValidation('frequency')
        #              ]
