from aiogram import types, Dispatcher
from config import bot


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

async def quiz_3(call: types.CallbackQuery):
    question = "Лучший футболист в истории?"
    answers = [
        'Пелле',
        'Кройф',
        'Роналду',
        'Месси',
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        open_period=30,
    )
async def photo_mem2(call: types.CallbackQuery):
    photo2 = open("media/mem.png", 'rb')
    await bot.send_photo(call.from_user.id, photo=photo2)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(photo_mem2, text="button_call_3")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")
