from aiogram import types, Dispatcher
from keyboards import kb_client
from keyboards import menu_kb

#@dp.message_handler(commands = 'start')
async def start_fn(message : types.Message):
    await message.answer("Привіт, я бот для пошуку і завантаження креслень(blueprints) для Spaceflight simulator\nНапиши /help щоб дізнатись більше", reply_markup=kb_client)
#@dp.message_handler(commands = 'help')
async def help_fn(message : types.Message):
    await message.answer("Тицяй на кнопки", reply_markup=menu_kb)

def register_handlers_client(dp : Dispatcher):
        dp.register_message_handler(start_fn, commands='start')
        dp.register_message_handler(help_fn, commands='help')