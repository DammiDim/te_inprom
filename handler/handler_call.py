from telebot import types

from data.loader import bot
from data.texts import t_exhibition_submenu_4, t_exhibition_submenu_3, t_exhibition_submenu_2, t_exhibition_submenu_1, \
    t_register_submenu_vip, t_register_submenu_visitor, t_register_submenu_delegate, t_register_submenu_media, \
    t_upcoming_proj_submenu_bioprom, t_upcoming_proj_submenu_innoprom_ca, t_upcoming_proj_submenu_innoprom_sa


# @bot.callback_query_handler(func=lambda call: 'exhibition' in call.data)
# def exhibition_submenu(call):
#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#
#     markup = types.InlineKeyboardMarkup(row_width=1).add(
#         types.InlineKeyboardButton('Назад', callback_data='to_back_exhibition'), )
#
#     if call.data == 'exhibition_1':
#         bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                               text='Цифровое производство',
#                               reply_markup=markup)
#     elif call.data == 'exhibition_2':
#         bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                               text='Металлообработка',
#                               reply_markup=markup)
#     elif call.data == 'exhibition_3':
#         bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                               text='Транспортное машиностроение',
#                               reply_markup=markup)
#     elif call.data == 'exhibition_4':
#         bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                               text='Технологии для городов',
#                               reply_markup=markup)
#     elif call.data == 'exhibition_5':
#         bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                               text='Промышленные IT',
#                               reply_markup=markup)
#     elif call.data == 'exhibition_6':
#         bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                               text='Технологии для энергетики',
#                               reply_markup=markup)
#     elif call.data == 'exhibition_7':
#         bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                               text='Новые материалы',
#                               reply_markup=markup)
#     elif call.data == 'exhibition_8':
#         bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                               text='Производство компонентов',
#                               reply_markup=markup)
#     elif call.data == 'exhibition_9':
#         bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                               text='Медицинская техника и оборудование для реабилитации',
#                               reply_markup=markup)
#     elif call.data == 'exhibition_10':
#         bot.edit_message_text(chat_id=chat_id, message_id=message_id,
#                               text='Автоматизация и робототехника',
#                               reply_markup=markup)


@bot.callback_query_handler(func=lambda call: 'exhibitors' in call.data)
def exhibitors_submenu(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton('Назад', callback_data='to_back_exhibitors'), )

    if call.data == 'exhibitors_1':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibition_submenu_1,
                              reply_markup=markup)

    elif call.data == 'exhibitors_2':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibition_submenu_2,
                              reply_markup=markup)

    elif call.data == 'exhibitors_3':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibition_submenu_3,
                              reply_markup=markup)

    elif call.data == 'exhibitors_4':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibition_submenu_4,
                              reply_markup=markup)


@bot.callback_query_handler(func=lambda call: 'register' in call.data)
def register_submenu(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton('Назад', callback_data='to_back_register'), )

    if call.data == 'register_vip':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_register_submenu_vip,
                              reply_markup=markup)
        # https: // expo.innoprom.com / register / vip /

    elif call.data == 'register_visitor':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_register_submenu_visitor,
                              reply_markup=markup)
        # https: // expo.innoprom.com / register / visitor /


    elif call.data == 'register_delegate':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_register_submenu_delegate,
                              reply_markup=markup)
        # https: // expo.innoprom.com / register / delegate /

    elif call.data == 'register_media':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_register_submenu_media,
                              reply_markup=markup)
        # https: // expo.innoprom.com / register / press /


@bot.callback_query_handler(func=lambda call: 'upcoming_proj' in call.data)
def upcoming_proj_submenu(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton('Назад', callback_data='to_back_upcoming_proj'), )

    if call.data == 'upcoming_proj_bioprom':
        markup.add(types.InlineKeyboardButton('Посетить сайт', url=r'https://biopromforum.ru/'), )
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_upcoming_proj_submenu_bioprom,
                              reply_markup=markup)

    elif call.data == 'upcoming_proj_innoprom_sa':
        markup.add(types.InlineKeyboardButton('Посетить сайт', url=r'https://ksabm.com/'), )
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_upcoming_proj_submenu_innoprom_sa,
                              reply_markup=markup)

    elif call.data == 'upcoming_proj_innoprom_ca':
        markup.add(types.InlineKeyboardButton('Скоро будет', callback_data='a'), )
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_upcoming_proj_submenu_innoprom_ca,
                              reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'tobook')
def tobook_submenu(call):
    text = 'Тут должна случиться магия, но у нас кончилась волшебная пыльца *('
    bot.answer_callback_query(call.id, text, show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data)
def invalid_request(call):
    text = 'Запрос не был выполнен, так как истёк срок его отправки или он был некорректно сформирован.'
    bot.answer_callback_query(call.id, text, show_alert=True)
