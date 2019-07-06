"""
Main logic for Telegram Bot
"""
from telebot import TeleBot
from Revorate import settings


telegram_bot = TeleBot(settings.API_TOKEN)
