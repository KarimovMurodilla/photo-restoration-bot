from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .answering import CallbackQueryMiddleware


if __name__ == "middlewares":
    # устанавливаем мидлвары
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(CallbackQueryMiddleware())