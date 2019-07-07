from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from .strings import get_string
from revoratebot.models import User, Department

_keyboards_ru = {
    'remove': ReplyKeyboardRemove()
}
_keyboards_uz = {
    'remove': ReplyKeyboardRemove()
}
_keyboards_en = {
    'remove': ReplyKeyboardRemove()
}

_default_value = ReplyKeyboardMarkup(resize_keyboard=True)
_default_value.add('no_keyboard')


def _create_keyboard(row_width=3):
    return ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)


def get_keyboard(key, language='ru'):
    if key == 'remove':
        return ReplyKeyboardRemove()
    elif key == 'registration.languages':
        language_keyboard = _create_keyboard(row_width=1)
        language_keyboard.add(get_string('languages.ru', language),
                              get_string('languages.en', language),
                              get_string('languages.uz', language))
        return language_keyboard
    else:
        return _default_value


def get_main_keyboard_by_user_role(user: User):
    language = user.language
    drivers_code = Department.DefaultNames.DRIVERS
    dispatchers_code = Department.DefaultNames.DISPATCHERS
    if user.department:
        if user.department == drivers_code:
            keyboard = _create_keyboard(row_width=2)
            keyboard.add(get_string('menu.put_estimate', language),
                         get_string('menu.sos', language))
        elif user.department == dispatchers_code:
            keyboard = _create_keyboard(row_width=1)
            keyboard.add(get_string('menu.put_estimate', language))
        else:
            return None
    else:
        if not user.is_manager:
            return None
        keyboard = _create_keyboard(row_width=1)
        keyboard.add(get_string('menu.ratings', language))
    keyboard.add(get_string('menu.settings', language))
    return keyboard
