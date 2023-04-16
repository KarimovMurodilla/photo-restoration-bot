from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


# Этот middleware предназначен для быстрого ответа на callback запрос, чтобы кнопка долго не загружался
class CallbackQueryMiddleware(BaseMiddleware):
    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        await callback_query.answer()
