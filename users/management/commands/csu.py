from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            telegram_account='khaidoukova',
            chat_id='559091554',
            is_staff=True,
            is_superuser=True

        )

        user.set_password('320670')
        user.save()
        print('superuser created')
