from aiogram import types


def groups(): # кнопки для меню
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Подобрать группу", callback_data="choose_group")
    btn2 = types.InlineKeyboardButton(text="Список групп", callback_data="groups_list")
    menu.add(btn1, btn2)

    return menu