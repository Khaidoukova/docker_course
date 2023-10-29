import requests
from django.conf import settings
from users.models import User

TOKEN = settings.TG_API


def tg_send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=params)
    return


