import os
import json
from revoratebot.models import Rating, SosSignal

_basedir = os.path.abspath(os.path.dirname(__file__))

# Load strings from json
# Russian language
_strings_ru = json.loads(open(os.path.join(_basedir, 'strings_ru.json'), 'r', encoding='utf8').read())

# Uzbek language
_strings_uz = json.loads(open(os.path.join(_basedir, 'strings_uz.json'), 'r', encoding='utf8').read())

# English language
_strings_en = json.loads(open(os.path.join(_basedir, 'strings_en.json'), 'r', encoding='utf8').read())


def get_string(key, language='ru'):
    if language == 'ru':
        return _strings_ru.get(key, 'no_string')
    elif language == 'uz':
        return _strings_uz.get(key, 'no_string')
    elif language == 'en':
        return _strings_en.get(key, 'no_string')
    else:
        raise Exception('Invalid language')


def estimate_value_from_string(string, language):
    if get_string('estimates.value_1', language) in string:
        return Rating.Values.VERY_LOW
    elif get_string('estimates.value_2', language) in string:
        return Rating.Values.LOW
    elif get_string('estimates.value_3', language) in string:
        return Rating.Values.MEDIUM
    elif get_string('estimates.value_4', language) in string:
        return Rating.Values.HIGH
    elif get_string('estimates.value_5', language) in string:
        return Rating.Values.VERY_HIGH
    else:
        return None


def string_from_sos_signal(sos_signal: SosSignal, sender, language):
    datetime = sos_signal.created_at.strftime('%d.%m.%Y %H:%M')
    sos_message_content = ""
    sos_message_content += get_string('sos.new_signal', language)
    sos_message_content += '\n'
    sos_message_content += get_string('sos.sender', language).format(name=sender.name)
    sos_message_content += '\n'
    sos_message_content += get_string('sos.sent_at', language).format(date=datetime)
    return sos_message_content
