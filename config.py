from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
AD = config("ADMINS")
PAYMENTS_TOKEN = config("PAYMENTS_TOKEN")
TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMINS = (537862455, )
