from telebot import types

from data.loader import bot
from data.texts import *


@bot.callback_query_handler(func=lambda call: 'exhibitors' in call.data)
def exhibitors_submenu(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton('Назад', callback_data='to_back_exhibitors'), )

    if call.data == 'exhibitors_1':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibitors_submenu_1,
                              reply_markup=markup)

    elif call.data == 'exhibitors_2':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibitors_submenu_2,
                              reply_markup=markup)

    elif call.data == 'exhibitors_3':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibitors_submenu_3,
                              reply_markup=markup)

    elif call.data == 'exhibitors_4':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibitors_submenu_4,
                              reply_markup=markup)


@bot.callback_query_handler(func=lambda call: 'register' in call.data)
def register_submenu(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton('Назад', callback_data='to_back_register'), )

    if call.data == 'register_vip':
        markup.add(types.InlineKeyboardButton('Посетить сайт',
                                              url=r'https://expo.innoprom.com/register/vip/'), )
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_register_submenu_vip,
                              reply_markup=markup)

    elif call.data == 'register_visitor':
        markup.add(types.InlineKeyboardButton('Посетить сайт',
                                              url=r'https://expo.innoprom.com/register/visitor/'), )
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_register_submenu_visitor,
                              reply_markup=markup)

    elif call.data == 'register_delegate':
        markup.add(types.InlineKeyboardButton('Посетить сайт',
                                              url=r'https://expo.innoprom.com/register/delegate/'), )
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_register_submenu_delegate,
                              reply_markup=markup)

    elif call.data == 'register_media':
        markup.add(types.InlineKeyboardButton('Посетить сайт',
                                              url=r'https://expo.innoprom.com/register/press/'), )
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_register_submenu_media,
                              reply_markup=markup)


@bot.callback_query_handler(func=lambda call: 'upcoming_proj' in call.data)
def upcoming_proj_submenu(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton('Назад', callback_data='to_back_upcoming_proj'), )

    if call.data == 'upcoming_proj_bioprom':
        markup.add(types.InlineKeyboardButton('Посетить сайт',
                                              url=r'https://biopromforum.ru/'), )
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_upcoming_proj_submenu_bioprom,
                              reply_markup=markup)

    elif call.data == 'upcoming_proj_innoprom_sa':
        markup.add(types.InlineKeyboardButton('Посетить сайт',
                                              url=r'https://ksabm.com/'), )
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_upcoming_proj_submenu_innoprom_sa,
                              reply_markup=markup)

    elif call.data == 'upcoming_proj_innoprom_ca':
        markup.add(types.InlineKeyboardButton('Скоро будет',
                                              callback_data='a'), )
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_upcoming_proj_submenu_innoprom_ca,
                              reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'tobook')
def tobook_submenu(call):
    text = 'Тут должна случиться магия, но у нас кончилась волшебная пыльца *('
    bot.answer_callback_query(call.id, text, show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data)
def invalid_request(call):
    bot.answer_callback_query(call.id, t_invalid_request, show_alert=True)
