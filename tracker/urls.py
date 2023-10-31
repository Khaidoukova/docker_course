from django.urls import path

from tracker.apps import TrackerConfig

from tracker.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitsListAPIView

app_name = TrackerConfig.name

urlpatterns = [

    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_get'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('habit/public/', PublicHabitsListAPIView.as_view(), name='public_habits'), ]
