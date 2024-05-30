from telebot import types


def exhibition_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Цифровое производство', callback_data='exhibition_1'),
        types.InlineKeyboardButton('Металлообработка', callback_data='exhibition_2'),
        types.InlineKeyboardButton('Транспортное машиностроение', callback_data='exhibition_3'),
        types.InlineKeyboardButton('Технологии для городов', callback_data='exhibition_4'),
        types.InlineKeyboardButton('Промышленные IT', callback_data='exhibition_5'),
        types.InlineKeyboardButton('Технологии для энергетики', callback_data='exhibition_6'),
        types.InlineKeyboardButton('Новые материалы', callback_data='exhibition_7'),
        types.InlineKeyboardButton('Производство компонентов', callback_data='exhibition_8'),
        types.InlineKeyboardButton('Медицинская техника и оборудование для реабилитации', callback_data='exhibition_9'),
        types.InlineKeyboardButton('Автоматизация и робототехника', callback_data='exhibition_10'),
    )

    return markup


def register_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Посетитель', web_app=types.WebAppInfo('https://expo.innoprom.com/register/visitor/')),
        types.InlineKeyboardButton('VIP-участие', web_app=types.WebAppInfo('https://expo.innoprom.com/register/visitor/')),
        types.InlineKeyboardButton('Делегат', web_app=types.WebAppInfo('https://expo.innoprom.com/register/delegate/')),
        types.InlineKeyboardButton('СМИ', web_app=types.WebAppInfo('https://expo.innoprom.com/register/press/')),
    )

    return markup


def exhibitors_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Рекламные и PR опции', callback_data='exhibitors_1'),
        types.InlineKeyboardButton('АРЕНДА ПЕРЕГОВОРНОЙ КОМНАТЫ', callback_data='exhibitors_2'),
        types.InlineKeyboardButton('ОХРАНА ВЫСТАВОЧНЫХ СТЕНДОВ', callback_data='exhibitors_3'),
        types.InlineKeyboardButton('ТРЕВЕЛ-СОПРОВОЖДЕНИЕ', callback_data='exhibitors_4'),
    )

    return markup

