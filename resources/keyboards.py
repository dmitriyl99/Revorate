from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

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


def get_keyboard(key, language='ru'):
    if language == 'ru':
        return _keyboards_ru.get(key, _default_value)
    elif language == 'uz':
        return _keyboards_uz.get(key, _default_value)
    elif language == 'en':
        return _keyboards_en.get(key, _default_value)
    else:
        raise Exception('Invalid language')
