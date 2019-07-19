from . import telegram_bot
from .utils import Access, Navigation
from core.managers import users, ratings
from resources import strings, keyboards
from telebot.types import Message


def _to_departments_select(user, chat_id):
    departments = user.department.company.department_set.all()
    departments_message = strings.get_string('estimates.select_department', user.language)
    departments_keyboard = keyboards.keyboard_from_departments_list(departments, user.language)
    telegram_bot.send_message(chat_id, departments_message, reply_markup=departments_keyboard)
    telegram_bot.register_next_step_handler_by_chat_id(chat_id, departments_processor, user=user)


def _to_users(user, chat_id, department_name, error_callback=None):
    department_users = users.find_users_by_department_name(department_name, user.id, user.department.company_id)
    if not department_users:
        if error_callback:
            error_callback()
        return
    users_message = strings.get_string('estimates.select_user', user.language)
    users_keyboard = keyboards.keyboard_from_users_list(department_users, user.language)
    telegram_bot.send_message(chat_id, users_message, reply_markup=users_keyboard)
    telegram_bot.register_next_step_handler_by_chat_id(chat_id, users_processor, user=user)


def _to_estimates(user, chat_id, selected_user):
    estimates_message = strings.get_string('estimates.select_estimate', user.language)
    estimates_keyboard = keyboards.get_keyboard('estimates.estimates', user.language)
    telegram_bot.send_message(chat_id, estimates_message, reply_markup=estimates_keyboard)
    telegram_bot.register_next_step_handler_by_chat_id(chat_id, estimates_processor, user=user,
                                                       selected_user=selected_user)


@telegram_bot.message_handler(content_types=['text'], func=Access.estimates)
def estimates_handler(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user = users.get_user_by_telegram_id(user_id)
    _to_departments_select(user, chat_id)


def departments_processor(message: Message, **kwargs):
    user = kwargs.get('user')
    chat_id = message.chat.id

    def error():
        error_message = strings.get_string('estimates.select_department', user.language)
        telegram_bot.send_message(chat_id, error_message)
        telegram_bot.register_next_step_handler_by_chat_id(chat_id, departments_processor, user=user)

    if not message.text:
        error()
        return
    if strings.get_string('go_back', user.language) in message.text:
        Navigation.to_main_menu(user, chat_id)
        return
    _to_users(user, chat_id, message.text, error_callback=error)


def users_processor(message: Message, **kwargs):
    user = kwargs.get('user')
    chat_id = message.chat.id

    def error():
        error_message = strings.get_string('estimates.select_user', user.language)
        telegram_bot.send_message(chat_id, error_message)
        telegram_bot.register_next_step_handler_by_chat_id(chat_id, users_processor, user=user)

    if not message.text:
        error()
        return
    if strings.get_string('go_back', user.language) in message.text:
        _to_departments_select(user, chat_id)
        return
    selected_user = users.find_user_by_name(message.text)
    if not selected_user:
        error()
        return
    _to_estimates(user, chat_id, selected_user)


def estimates_processor(message: Message, **kwargs):
    user = kwargs.get('user')
    selected_user = kwargs.get('selected_user')
    chat_id = message.chat.id

    def error():
        error_message = strings.get_string('estimate.select_estimate', user.language)
        telegram_bot.send_message(chat_id, error_message)
        telegram_bot.register_next_step_handler_by_chat_id(chat_id, estimates_processor, user=user,
                                                           selected_user=selected_user)

    if not message.text:
        error()
        return
    if strings.get_string('go_back', user.language) in message.text:
        _to_users(user, chat_id, user.department.name)
        return
    value = strings.estimate_value_from_string(message.text, user.language)
    if not value:
        error()
        return
    comment_message = strings.get_string('estimates.comment', user.language)
    if value < 4:
        comment_templates = selected_user.department.comment_templates.all()
        if len(comment_templates) > 0:
            comment_message = strings.get_string('estimates.comment_with_templates', user.language)
            comments_keyboard = keyboards.keyboard_from_comments_templates(comment_templates, user.language)
            telegram_bot.send_message(chat_id, comment_message, reply_markup=comments_keyboard)
        else:
            telegram_bot.send_message(chat_id, comment_message)
    else:
        telegram_bot.send_message(chat_id, comment_message)
    telegram_bot.register_next_step_handler_by_chat_id(chat_id, comments_processor, user=user,
                                                       selected_user=selected_user,
                                                       estimate=value)


def comments_processor(message: Message, **kwargs):
    user = kwargs.get('user')
    selected_user = kwargs.get('selected_user')
    estimate_value = kwargs.get('estimate')
    chat_id = message.chat.id

    def error():
        error_message = strings.get_string('estimates.comment', user.language)
        telegram_bot.send_message(chat_id, error_message)
        telegram_bot.register_next_step_handler_by_chat_id(chat_id, comments_processor, user=user,
                                                           selected_user=selected_user,
                                                           estimate=estimate_value)

    if not message.text:
        error()
        return
    if strings.get_string('go_back', user.language) in message.text:
        _to_estimates(user, chat_id, selected_user)
        return
    comment = message.text
    ratings.create_rating(user, selected_user, estimate_value, comment)
    success_message = strings.get_string('estimates.success', user.language).format(name=selected_user.name,
                                                                                    department=selected_user.department.name)
    Navigation.to_main_menu(user, chat_id, message_text=success_message)
