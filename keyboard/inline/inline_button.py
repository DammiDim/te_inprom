from telebot import types


def vip_participation_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Стать VIP-участником ', url='https://expo.innoprom.com/for-participants/vip')
    )

    return markup


def register_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Посетитель', callback_data='register_visitor'),
        types.InlineKeyboardButton('VIP-участие', callback_data='register_vip'),
        types.InlineKeyboardButton('Делегат', callback_data='register_delegate'),
        types.InlineKeyboardButton('СМИ', callback_data='register_media'),
    )

    return markup


def exhibitors_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Фотосопровождение', callback_data='exhibitors_1'),
        types.InlineKeyboardButton('Рекламные и PR опции', callback_data='exhibitors_2'),
        types.InlineKeyboardButton('Аренда переговорной комнаты', callback_data='exhibitors_3'),
        types.InlineKeyboardButton('Охрана выставочных стендов', callback_data='exhibitors_4'),
        types.InlineKeyboardButton('Тревел-сопровождение', callback_data='exhibitors_5'),
        types.InlineKeyboardButton('INNOPROM Cafeteria', callback_data='exhibitors_6'),
    )

    return markup


def upcoming_projects_btn():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('БИОПРОМ (БИОТЕХМЕД и INNOFOOD) ', callback_data='upcoming_proj_bioprom'),
        types.InlineKeyboardButton('ИННОПРОМ. Саудовская Аравия', callback_data='upcoming_proj_innoprom_sa'),
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
        types.InlineKeyboardButton(
            text='Открыть карту',
            url=r'https://yandex.ru/maps/54/yekaterinburg/?from=mapframe&ll=60.758613%2C56'
                r'.767139&mode=usermaps&source=mapframe&um=constructor'
                r'%3Ad5c2c639720f2a59d9f1cc7f456f74e5600c40aba593c20a16e5d0b4f0e12859'
                r'&utm_source=mapframe&z=14'),
    )

    return markup
