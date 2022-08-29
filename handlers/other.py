from aiogram import types, Dispatcher


#@dp.message_handler()
async def echo(message : types.Message):
    await message.answer("Я тебе не розумію")

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo)