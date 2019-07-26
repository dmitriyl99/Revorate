"""
Main logic for Telegram Bot
"""
from telebot import TeleBot
from Revorate import settings as app_settings


telegram_bot = TeleBot(app_settings.API_TOKEN)

from . import registration, estimates, managers, settings, sos
