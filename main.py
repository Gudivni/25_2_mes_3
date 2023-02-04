import logging
from config import dp, bot, ADMINS
from aiogram.utils import executor
from handlers import client, callback, extra, admin, fsm_admin_mentor, FSM_Find_Mentors, notification, pay
from database.bot_db_mentors import sql_create
import asyncio


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()
    await bot.send_message(chat_id=ADMINS[0],
                           text="Bot started!")

client.register_handlers_client(dp)
pay.register_handlers_pay(dp)
callback.register_handlers_callback(dp)
fsm_admin_mentor.register_handlers_anketa(dp)
admin.register_handlers_admin(dp)
FSM_Find_Mentors.register_handlers_find_mentors(dp)
notification.register_handlers_notification(dp)
extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
