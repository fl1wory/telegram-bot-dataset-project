from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

help_bt = KeyboardButton('/help')

kb_client = ReplyKeyboardMarkup()
kb_client.add(help_bt)