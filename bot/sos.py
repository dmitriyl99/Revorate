from . import telegram_bot
from .utils import Access, Helpers
from resources import strings
from telebot.types import Message
from core.managers import users, sos


@telegram_bot.message_handler(content_types=['location'], func=Access.sos)
def sos_handler(message: Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    user_id = message.from_user.id
    chat_id = message.chat.id
    user = users.get_user_by_telegram_id(user_id)
    sos_signal = sos.create_sos(user, latitude, longitude)
    success_message = strings.get_string('sos.success', user.language)
    telegram_bot.send_message(chat_id, success_message)
    Helpers.send_sos_signal_to_managers(sos_signal, user)
