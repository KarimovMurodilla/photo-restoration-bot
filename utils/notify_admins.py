import logging

from aiogram import Dispatcher

from data.config import ADMINS


# Отправляем уведомление об запуске бота для админов
async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
