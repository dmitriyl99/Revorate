from revoratebot.models import User
from typing import Optional


def get_user_by_token(token: str) -> Optional[User]:
    try:
        user = User.objects.filter(token=token)[0]
    except IndexError:
        return None
    return user


def get_user_by_telegram_id(user_id: int) -> Optional[User]:
    try:
        user = User.objects.filter(telegram_user_id=user_id)[0]
    except IndexError:
        return None
    return user


def confirm_user(user: User, telegram_user_id):
    if user.confirmed:
        return False
    user.confirmed = True
    user.telegram_user_id = telegram_user_id
    user.save()
    return True


def set_user_language(user: User, language):
    user.language = language
    user.save()
