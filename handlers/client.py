from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keyboards.client_kb import start_markup
from time import sleep


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Доброго времени суток {message.from_user.first_name}", reply_markup=start_markup)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Учение о костях - называется:"
    answers = [
        "Микробиология",
        "остеология",
        "миология",
        "гистология",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=30,
        reply_markup=markup
    )

async def photo_mem(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT>>", callback_data='button_call_3')
    markup.add(button_call_3)
    photo = open("media/mem.png", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)
    await message.answer_photo(photo)


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id,  message.reply_to_message.message_id)
    else:
        await message.answer("Укажи кого закрепить!")


async def dice(message: types.Message):
    await message.answer('Твой ход')
    user_move = await message.answer_dice()
    sleep(5)
    await message.answer('Мой ход')
    bot_move = await message.answer_dice()
    sleep(5)
    if user_move.dice.value > bot_move.dice.value:
        await message.answer('Ты победил!')
    elif user_move.dice.value < bot_move.dice.value:
        await message.answer('Я выйграл!')
    elif user_move.dice.value == bot_move.dice.value:
        await message.answer('Ничья!')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(photo_mem, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix="!")
    dp.register_message_handler(dice, commands=['dice'])
