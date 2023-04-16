from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, BASE_DIR
from keyboards.inline import inline_buttons

from utils.misc.restoration.colorizer import Colorizer


@dp.message_handler(content_types='photo', state='*')
async def send_result_photo(message: types.Message):
    msg = await message.answer("Идёт обработка...")
    img_dir = BASE_DIR / f'images/downloads/{message.from_user.id}.jpg'
    await message.photo[-1].download(img_dir)
    
    col = Colorizer()
    await col.colorize_image(message.from_user.id)

    await message.answer_photo(types.InputFile(col.photo_dir))

    await msg.delete()