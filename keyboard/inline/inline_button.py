from telebot import types


# def exhibition_btn():
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     markup.add(
#         types.InlineKeyboardButton('Цифровое производство', callback_data='exhibition_1'),
#         types.InlineKeyboardButton('Металлообработка', callback_data='exhibition_2'),
#         types.InlineKeyboardButton('Транспортное машиностроение', callback_data='exhibition_3'),
#         types.InlineKeyboardButton('Технологии для городов', callback_data='exhibition_4'),
#         types.InlineKeyboardButton('Промышленные IT', callback_data='exhibition_5'),
#         types.InlineKeyboardButton('Технологии для энергетики', callback_data='exhibition_6'),
#         types.InlineKeyboardButton('Новые материалы', callback_data='exhibition_7'),
#         types.InlineKeyboardButton('Производство компонентов', callback_data='exhibition_8'),
#         types.InlineKeyboardButton('Медицинская техника и оборудование для реабилитации', callback_data='exhibition_9'),
#         types.InlineKeyboardButton('Автоматизация и робототехника', callback_data='exhibition_10'),
#     )
#
#     return markup


def vip_participation_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Стать VIP-участником ', url='https://expo.innoprom.com/for-participants/vip')
    )

    return markup


def register_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Посетитель',  callback_data='register_visitor'),
        types.InlineKeyboardButton('VIP-участие', callback_data='register_vip'),
        types.InlineKeyboardButton('Делегат', callback_data='register_delegate'),
        types.InlineKeyboardButton('СМИ', callback_data='register_media'),
    )

    return markup


# def register_btn():
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     markup.add(
#         types.InlineKeyboardButton('Посетитель',
#                                    web_app=types.WebAppInfo('https://expo.innoprom.com/register/visitor/')),
#         types.InlineKeyboardButton('VIP-участие',
#                                    web_app=types.WebAppInfo('https://expo.innoprom.com/register/visitor/')),
#         types.InlineKeyboardButton('Делегат',
#                                    web_app=types.WebAppInfo('https://expo.innoprom.com/register/delegate/')),
#         types.InlineKeyboardButton('СМИ',
#                                    web_app=types.WebAppInfo('https://expo.innoprom.com/register/press/')),
#     )
#
#     return markup


def exhibitors_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Рекламные и PR опции', callback_data='exhibitors_1'),
        types.InlineKeyboardButton('АРЕНДА ПЕРЕГОВОРНОЙ КОМНАТЫ', callback_data='exhibitors_2'),
        types.InlineKeyboardButton('ОХРАНА ВЫСТАВОЧНЫХ СТЕНДОВ', callback_data='exhibitors_3'),
        types.InlineKeyboardButton('ТРЕВЕЛ-СОПРОВОЖДЕНИЕ', callback_data='exhibitors_4'),
    )

    return markup


def upcoming_projects_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('БИОПРОМ (БИОТЕХМЕД и INNOFOOD) ', callback_data='upcoming_proj_bioprom'),
        types.InlineKeyboardButton('ИННОПРОМ Саудовская Аравия', callback_data='upcoming_proj_innoprom_sa'),
        types.InlineKeyboardButton('ИННОПРОМ. Центральная Азия', callback_data='upcoming_proj_innoprom_ca'),
    )

    return markup

def dl_app_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(text='Скачать мобильное приложение',
                                   url=r'https://expo.innoprom.com/mobile-application'),
    )

    return markup


def address_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(text='Открыть карту',
                                   url=r'https://yandex.ru/maps/54/yekaterinburg/?from=mapframe&ll=60.758613%2C56'
                                       r'.767139&mode=usermaps&source=mapframe&um=constructor'
                                       r'%3Ad5c2c639720f2a59d9f1cc7f456f74e5600c40aba593c20a16e5d0b4f0e12859'
                                       r'&utm_source=mapframe&z=14'),
    )

    return markup
