from telebot import types


def vip_participation_btn():
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton('Стать VIP-участником ', url='https://expo.innoprom.com/for-participants/vip')
    )

    return _markup


def register_btn():
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton('Посетитель', callback_data='register_visitor'),
        types.InlineKeyboardButton('VIP-участие', callback_data='register_vip'),
        types.InlineKeyboardButton('Делегат', callback_data='register_delegate'),
        types.InlineKeyboardButton('СМИ', callback_data='register_media'),
    )

    return _markup


def exhibitors_btn():
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton('Фотосопровождение', callback_data='exhibitors_1'),
        types.InlineKeyboardButton('Рекламные и PR опции', callback_data='exhibitors_2'),
        types.InlineKeyboardButton('Аренда переговорной комнаты', callback_data='exhibitors_3'),
        types.InlineKeyboardButton('Охрана выставочных стендов', callback_data='exhibitors_4'),
        types.InlineKeyboardButton('Тревел-сопровождение', callback_data='exhibitors_5'),
        types.InlineKeyboardButton('INNOPROM Cafeteria', callback_data='exhibitors_6'),
    )

    return _markup


def upcoming_projects_btn():
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton('БИОПРОМ (БИОТЕХМЕД и INNOFOOD) ', callback_data='upcoming_proj_bioprom'),
        types.InlineKeyboardButton('ИННОПРОМ. Центральная Азия', callback_data='upcoming_proj_innoprom_ca'),
    )
    # todo temporarily
    # types.InlineKeyboardButton('ИННОПРОМ. Саудовская Аравия', callback_data='upcoming_proj_innoprom_sa'),
    return _markup


def dl_app_btn():
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton(text='Скачать мобильное приложение',
                                   url=r'https://expo.innoprom.com/mobile-application'),
    )
    return _markup


def spikes_btn():
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton(text='Актуальный список будет позже, как пример',
                                   url='https://expo.innoprom.com/speakers/'),
    )
    return _markup


def business_program_btn():
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton(text='Деловая программа',
                                   url='https://expo.innoprom.com/business-program/'),
    )
    return _markup


def organizers_btn():
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton(
            text='Business Event',
            url=r'https://business-event.com/ '),

        types.InlineKeyboardButton(
            text='Министерство промышленности и торговли РФ',
            url=r'https://minpromtorg.gov.ru/'),

        types.InlineKeyboardButton(
            text='Правительство Свердловской области',
            url=r'https://midural.ru/'),
    )
    return _markup


def address_btn():
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton(
            text='Открыть карту',
            url=r'https://yandex.ru/maps/-/CDrWYZzc')
    )
    return _markup
