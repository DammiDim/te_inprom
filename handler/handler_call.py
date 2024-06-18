from telebot import types
from telebot.types import InputMediaPhoto

from data.loader import bot
from data.texts import *


@bot.callback_query_handler(func=lambda call: 'exhibitors' in call.data)
def exhibitors_submenu(call):
    _chat_id = call.message.chat.id
    _message_id = call.message.message_id

    _photo = open('img/img_exhibitors.png', 'rb')

    _markup = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton('Назад', callback_data='to_back_exhibitors'), )

    _text = ''

    if call.data == 'exhibitors_1':
        _text = t_exhibitors_submenu_1

    elif call.data == 'exhibitors_2':
        _text = t_exhibitors_submenu_2

    elif call.data == 'exhibitors_3':
        _text = t_exhibitors_submenu_3

    elif call.data == 'exhibitors_4':
        _text = t_exhibitors_submenu_4

    elif call.data == 'exhibitors_5':
        _text = t_exhibitors_submenu_5

    elif call.data == 'exhibitors_6':
        _text = t_exhibitors_submenu_6

    _media = InputMediaPhoto(media=_photo, caption=_text, parse_mode='html')
    bot.edit_message_media(media=_media,
                           chat_id=_chat_id,
                           message_id=_message_id,
                           reply_markup=_markup)
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: 'register' in call.data)
def register_submenu(call):
    _chat_id = call.message.chat.id
    _message_id = call.message.message_id

    _photo = open('img/img_register.png', 'rb')

    _markup = types.InlineKeyboardMarkup(row_width=1)
    _back_btn = types.InlineKeyboardButton('Назад', callback_data='to_back_register')
    _more_btn = types.InlineKeyboardButton('Подробнее,', callback_data='none')
    _text = ''

    if call.data == 'register_vip':
        _more_btn = types.InlineKeyboardButton('Подробнее', url=r'https://expo.innoprom.com/register/vip/')
        _text = t_register_submenu_vip

    elif call.data == 'register_visitor':
        _more_btn = types.InlineKeyboardButton('Подробнее', url=r'https://expo.innoprom.com/register/visitor/')
        _text = t_register_submenu_visitor

    elif call.data == 'register_delegate':
        _more_btn = types.InlineKeyboardButton('Подробнее', url=r'https://expo.innoprom.com/register/delegate/')
        _text = t_register_submenu_delegate

    elif call.data == 'register_media':
        _more_btn = types.InlineKeyboardButton('Подробнее', url=r'https://expo.innoprom.com/register/press/')
        _text = t_register_submenu_media

    _markup.add(_more_btn, _back_btn)
    _media = InputMediaPhoto(media=_photo, caption=_text, parse_mode='html')
    bot.edit_message_media(media=_media,
                           chat_id=_chat_id,
                           message_id=_message_id,
                           reply_markup=_markup)
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: 'upcoming_proj' in call.data)
def upcoming_proj_submenu(call):
    _chat_id = call.message.chat.id
    _message_id = call.message.message_id

    _photo = open('img/img_upcoming_projects.png', 'rb')

    _markup = types.InlineKeyboardMarkup(row_width=1)
    _back_btn = types.InlineKeyboardButton('Назад', callback_data='to_back_upcoming_proj')
    _more_btn = types.InlineKeyboardButton('Подробнее,', callback_data='none')
    _text = ''

    if call.data == 'upcoming_proj_bioprom':
        _more_btn = types.InlineKeyboardButton('Подробнее', url=r'https://biopromforum.ru/')
        _text = t_upcoming_proj_submenu_bioprom

    elif call.data == 'upcoming_proj_innoprom_sa':
        _more_btn = types.InlineKeyboardButton('Подробнее', url=r'https://ksabm.com/')
        _text = t_upcoming_proj_submenu_innoprom_sa

    elif call.data == 'upcoming_proj_innoprom_ca':
        _more_btn = types.InlineKeyboardButton('Подробнее', url=r'https://tashkent.bigindustrialweek.com/ru/')
        _text = t_upcoming_proj_submenu_innoprom_ca

    _markup.add(_more_btn, _back_btn)
    _media = InputMediaPhoto(media=_photo, caption=_text, parse_mode='html')
    bot.edit_message_media(media=_media,
                           chat_id=_chat_id,
                           message_id=_message_id,
                           reply_markup=_markup)
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'tobook')
def tobook_submenu(call):
    # todo исправить текст
    _text = 'Тут должна случиться магия, но у нас кончилась волшебная пыльца *('
    bot.answer_callback_query(call.id, _text, show_alert=True)
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data)
def invalid_request(call):
    bot.answer_callback_query(call.id, t_invalid_request, show_alert=True)
