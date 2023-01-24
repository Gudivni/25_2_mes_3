from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINS
from keyboards import client_kb
from database.bot_db_mentors import sql_command_find_id_mentors


class FSMFindId(StatesGroup):
    Id = State()


async def fsm_id_m(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Доступ ограничен!")
    if message.chat.type == "private":
        await FSMFindId.Id.set()
        await message.answer("Имя ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в личке!")


async def find_id(message: types.Message, state: FSMContext):
    read = await sql_command_find_id_mentors(message.text)
    for res in read:
        await message.answer(f"ID = {res[0]},Name {res[1]}, Direction {res[2]}, Age {res[3]}, Group {res[4]}")
    await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Canceled")


def register_handlers_find_mentors(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals="cancel", ignore_case=True),
                                state="*")

    dp.register_message_handler(fsm_id_m, commands=['id'])
    dp.register_message_handler(find_id, state=FSMFindId.Id)
