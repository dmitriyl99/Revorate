from telebot.types import Message
from core.managers import users
from revoratebot.models import User, Department
from resources import strings
from typing import Optional


class Access:

    @staticmethod
    def _auth(message: Message) -> Optional[User]:
        user_id = message.from_user.id
        user = users.get_user_by_telegram_id(user_id)
        if not user:
            return None
        if user.department:
            if user.department.code_name != Department.DefaultNames.DISPATCHERS \
                    and user.department.code_name != Department.DefaultNames.DRIVERS:
                return None
        else:
            if not user.is_manager:
                return None
        return user

    @staticmethod
    def _private(message: Message):
        return message.chat.type != 'group' and message.chat.type != 'supergroup'

    @staticmethod
    def settings(message: Message):
        if not message.text:
            return False
        user = Access._auth(message)
        if not user:
            return False
        return Access._private(message) and strings.get_string('menu.settings', user.language) in message.text
