from rest_framework import status
from rest_framework.test import APITestCase

from tracker.models import Habit
from users.models import User
from rest_framework_simplejwt.tokens import AccessToken
from django.urls import reverse


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            telegram_account='test',
            email='test@test.com',
            password='1234',
            is_staff=False,
            is_active=True
        )

        self.token = f'Bearer {AccessToken.for_user(self.user)}'

        self.habit = Habit.objects.create(
            user=self.user,
            location='офис',
            time='12:00:00',
            action='сделать зарядку для глаз',
            is_pleasant=False,
            frequency=1,
            reward='выпить кофе',
            duration=1,
            public=True,
            next_reminder_date='2023-12-01'
        )

        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        data = {
            'user': self.user.pk,
            'location': 'дома',
            'time': '07:00:00',
            'action': 'выпить стакан воды с лимоном',
            'is_pleasant': False,
            'frequency': 1,
            'reward': 'выпить кофе',
            'duration': 1,
            'public': True,
            'next_reminder_date': '2023-12-01'
        }

        response = self.client.post(
            reverse('tracker:habit_create'),
            data=data,
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habit(self):
        response = self.client.get(
            reverse('tracker:habit_list'),
            HTTP_AUTHORIZATION=self.token
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        data = {
            'action': 'выпить воды',


        }

        response = self.client.patch(
            reverse('tracker:habit_update', kwargs={'pk': self.habit.pk}),
            data=data,
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Habit.objects.get(pk=self.habit.pk).action,
            'выпить воды'
        )

    def test_habit_destroy(self):

        response = self.client.delete(
            reverse('tracker:habit_delete', kwargs={'pk': self.habit.pk}),
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            list(Habit.objects.all()),
            []
        )

    def tearDown(self):
        self.user.delete()
        self.habit.delete()
