from aiogram import executor
from create_bot import dp

from handlers import client, other, admin

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True)