from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from config import bot
from keyboards.client_kb import start_markup
from time import sleep
from Parss.weath import parser
from Parss.new import parser


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


async def get_weather(message: types.Message):
    weather = parser()
    await message.answer(f"{weather['link']}\n{weather['date']}\ntemp {weather['now-weather']}\n{weather['now-feel']}\n"
                         f"{weather['now-desc']}\nЗаход {weather['astro-sunrise'][5:]}\nВосход "
                         f"{weather['astro-sunset'][6:]}\n"
                         f"Ветер {weather['now-info-item wind'][5:9]}\n"
                         f"Влажность {weather['now-info-item humidity'][9:]}",
                         parse_mode=ParseMode.HTML)


async def get_new_film(message: types.Message):
    film = parser()
    for i in film:
        await message.answer(
            f"{i['link']}\n\n"
            f"{i['title']}\n"
            f"#Y{i['date']}\n"
            f"#{i['genre']}\n"
            f"#{i['country']}"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(photo_mem, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix="!")
    dp.register_message_handler(dice, commands=['dice'])
    dp.register_message_handler(get_weather, commands=['weather'])
    dp.register_message_handler(get_new_film, commands=['newf'])
