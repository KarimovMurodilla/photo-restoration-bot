from aiogram.dispatcher.filters.state import State, StatesGroup


# Стейты для переключения между хендлерами в админ панели. Данный стейт используется для получения сообщений, от админа для рассылки
class InputMessage(StatesGroup):
    get_message = State()
