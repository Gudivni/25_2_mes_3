from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from decouple import config
import logging

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Доброго времени суток {message.from_user.first_name}")


@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    question = "На какой картинке изображена Эйфилевая башня?"
    answers = [
        '[1]',
        '[2]',
        '[3]',
        '[4]',
        '[5]',
        '[6]',
    ]

    photo = open("media/image.jpg", 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        open_period=30,
    )


@dp.message_handler(commands=['mem'])
async def photo_mem(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT>>", callback_data='button_call_3')
    markup.add(button_call_3)
    photo = open("media/mem.png", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)
    await message.answer_photo(photo)


@dp.callback_query_handler(text="button_call_3")
async def photo_mem2(call: types.CallbackQuery):
    photo2 = open("media/mem.png", 'rb')
    await bot.send_photo(call.from_user.id, photo=photo2)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(f"{int(message.text)**2}")
    else:
        await message.answer(f"{message.text}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
