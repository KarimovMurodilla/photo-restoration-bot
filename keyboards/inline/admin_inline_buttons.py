from aiogram import types


def admin_panel(): # кнопки для админ панели
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Выгрузить пользователей", callback_data="unload_users")
    btn2 = types.InlineKeyboardButton(text="Отправить сообщение пользователям", callback_data="send_to_users")
    menu.add(btn1, btn2)

    return menu