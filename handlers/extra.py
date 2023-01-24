from aiogram import types, Dispatcher
from config import bot
from random import choice
from config import ADMINS
from keyboards.client_kb import game_markup


async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(f"{int(message.text)**2}")
    elif message.text == 'game' and message.from_user.id in ADMINS:
        g = ['🎳', '🎲', '🏀', '🎯', '⚽', '🎰']
        await bot.send_dice(message.chat.id, emoji=choice(g), reply_markup=game_markup)
    elif message.text == '🎳':
        await bot.send_dice(message.chat.id, emoji='🎳')
    elif message.text == '🏀':
        await bot.send_dice(message.chat.id, emoji='🏀')
    elif message.text == '⚽':
        await bot.send_dice(message.chat.id, emoji='⚽')
    else:
        await message.answer(f"{message.text}")


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
