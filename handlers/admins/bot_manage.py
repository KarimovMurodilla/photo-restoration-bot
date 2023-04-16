from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from data.config import ADMINS
from keyboards.inline import admin_inline_buttons


# Обработчик сообщений для команды admin 
@dp.message_handler(chat_id=ADMINS, commands='admin', state='*')
async def add_project(message: types.Message, state: FSMContext):
    await message.answer("Выберите опцию", reply_markup=admin_inline_buttons.admin_panel())