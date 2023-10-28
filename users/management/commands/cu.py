from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            telegram_account='test_user',
            email='khaidoukova@inbox.ru',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('320670')
        user.save()
