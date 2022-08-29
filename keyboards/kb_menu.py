from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

add_b = KeyboardButton('/LOAD')

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.add(add_b)