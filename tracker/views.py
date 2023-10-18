from django.shortcuts import render
from rest_framework import generics

from tracker.models import Habit
from tracker.serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


