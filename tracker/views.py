from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from tracker.permissions import IsOwner, ReadOnly

from tracker.models import Habit
from tracker.serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitCreateAPIView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated | IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated | IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated | IsOwner]


class PublicHabitsListAPIView(generics.ListAPIView):
    queryset = Habit.objects.filter(public=True)
    serializer_class = HabitSerializer
    permission_classes = [ReadOnly]
