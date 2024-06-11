from telebot import types


def welcome_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                       row_width=3)
    btn0 = types.KeyboardButton('О выставке')
    btn1 = types.KeyboardButton('VIP участие')
    btn2 = types.KeyboardButton('Регистрация')

    btn3 = types.KeyboardButton('Ваше участие в 2025 году')

    btn5 = types.KeyboardButton('Время работы выставки')
    btn10 = types.KeyboardButton('Как добраться')
    btn4 = types.KeyboardButton('Схема выставки')

    btn8 = types.KeyboardButton('Назначить встречу на выставке')
    btn9 = types.KeyboardButton('Диалог с торгпредом')

    btn7 = types.KeyboardButton('ТОП-спикеры')
    btn11 = types.KeyboardButton('Экспонентам')
    btn6 = types.KeyboardButton('Деловая программа')

    btn12 = types.KeyboardButton('Контакты')
    btn13 = types.KeyboardButton('Ближайшие проекты')
    btn14 = types.KeyboardButton('Организаторы')

    btn15 = types.KeyboardButton('🔸 Задать вопрос 🔸')

    markup.add(btn0, btn1, btn2)
    markup.add(btn3)
    markup.add(btn5, btn10, )  # btn4
    markup.add(btn8, btn9)
    markup.add(btn6, btn11)  # btn7
    markup.add(btn12, btn13, btn14)
    markup.add(btn15)

    return markup
