import requests
from django.conf import settings
from users.models import User


def tg_get_updates(offset=None):
    params = {}
    if offset is not None:
        params = {'offset': offset}
    response = requests.get(f'https://api.telegram.org/bot{settings.Telegram_bot_API}/getUpdates', params=params)
    data = response.json()
    User.chat_id = data["result"][0]["message"]["chat"]["id"]


def tg_send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    requests.get(f'https://api.telegram.org/bot{settings.Telegram_bot_API}/sendMessage', params=params)
    return


