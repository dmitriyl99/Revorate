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
    if key == 'settings':
        settings_keyboard = _create_keyboard(row_width=1)
        settings_keyboard.add(get_string('settings.languages', language))
        return settings_keyboard
    else:
        return _default_value


def get_main_keyboard_by_user_role(user: User):
    language = user.language
    drivers_code = Department.DefaultNames.DRIVERS
    if user.department:
        keyboard = _create_keyboard(row_width=1)
        keyboard.add(get_string('menu.put_estimate', language))
        if user.department.code_name == drivers_code:
            keyboard.add(get_string('menu.sos', language))
    else:
        if not user.is_manager:
            return None
        keyboard = _create_keyboard(row_width=1)
        keyboard.add(get_string('menu.ratings', language))
    keyboard.add(get_string('menu.settings', language))
    return keyboard


def keyboard_by_user_language(user: User) -> ReplyKeyboardMarkup:
    keyboard = _create_keyboard(row_width=1)
    if user.language != 'ru':
        keyboard.add(get_string('languages.ru'))
    if user.language != 'uz':
        keyboard.add(get_string('languages.uz'))
    if user.language != 'en':
        keyboard.add(get_string('languages.en'))
    return keyboard
