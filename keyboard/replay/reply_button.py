from telebot import types


def welcome_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                       row_width=2)
    btn1 = types.KeyboardButton('О выставке')
    btn2 = types.KeyboardButton('Регистрация')
    btn3 = types.KeyboardButton('Забронировать площадь на 2025 год')
    btn4 = types.KeyboardButton('Схема выставки')
    btn5 = types.KeyboardButton('Время работы выставки')
    btn6 = types.KeyboardButton('Деловая программа')
    btn7 = types.KeyboardButton('ТОП-спикеры')
    btn8 = types.KeyboardButton('Назначить встречу на выставке')
    btn9 = types.KeyboardButton('Диалог с торгпредом')
    btn10 = types.KeyboardButton('Как добраться')
    btn11 = types.KeyboardButton('Экспонентам')
    btn12 = types.KeyboardButton('Контакты')
    btn13 = types.KeyboardButton('Ближайшие проекты')
    btn14 = types.KeyboardButton('Организаторы')
    markup.add(btn1, btn2)
    markup.add(btn3)
    markup.add(btn4, btn5, btn6, btn7)
    markup.add(btn8)
    markup.add(btn9, btn10, btn11, btn12, btn13, btn14)

    return markup

