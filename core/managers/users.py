from revoratebot.models import User, Department
from typing import Optional


def get_user_by_token(token: str) -> Optional[User]:
    """
    Get user by token
    :param token: token
    :return: User or None
    """
    try:
        user = User.objects.filter(token=token)[0]
    except IndexError:
        return None
    return user


def get_user_by_telegram_id(user_id: int) -> Optional[User]:
    """
    Get user by Telegram ID
    :param user_id: Telegram ID
    :return: User or None
    """
    try:
        user = User.objects.filter(telegram_user_id=user_id)[0]
    except IndexError:
        return None
    return user


def confirm_user(user: User, telegram_user_id):
    """
    Confirm user registration
    :param user: User
    :param telegram_user_id: User Telegram ID
    :return: If registration confirmed return True else return False
    """
    # If user registration already confirmed prevent access
    if user.confirmed:
        return False
    user.confirmed = True
    user.telegram_user_id = telegram_user_id
    user.save()
    return True


def set_user_language(user: User, language):
    """
    Set user language for Telegram Bot
    :param user: User
    :param language: language code, like 'ru', 'en' and 'uz'
    :return: void
    """
    user.language = language
    user.save()
