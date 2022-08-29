from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()


async def cm_start(message : types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Завантаж фото в редакторі')

async def load_photo(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Тепер введи назву')

async def load_name(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Тепер введи опис')

async def load_description(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await message.reply(str(data))
    await state.finish()

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands='LOAD', state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)