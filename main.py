from aiogram.utils import executor
from config import dp, bot, ADMINS
import logging
from handlers import client, callback, extra, admin, fsm_admin_mentor, FSM_Find_Mentors
from database.bot_db_mentors import sql_create

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_extra(dp)


async def on_startup(_):
    sql_create()
    await bot.send_message(chat_id=ADMINS[0],
                           text="Bot started!")

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsm_admin_mentor.register_handlers_anketa(dp)
admin.register_handlers_admin(dp)
FSM_Find_Mentors.register_handlers_find_mentors(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
