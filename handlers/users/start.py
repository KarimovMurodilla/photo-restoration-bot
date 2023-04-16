from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from keyboards.inline import inline_buttons


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    user = message.from_user
    db_user = await db.get_user(user.id) # Возвращает объект Users, в случае успеха

    if not db_user: #проверяем, если юзер нет на базе, то регистрируем его
        await db.reg_user(user.id, user.username, user.first_name)

    await message.answer("Привет! Отправь мне фото, я его раскрашу")