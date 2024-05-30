from telebot import types

from data.loader import bot


@bot.callback_query_handler(func=lambda call: 'exhibition' in call.data)
def exhibition_submenu(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton('Назад', callback_data='to_back_exhibition'), )

    if call.data == 'exhibition_1':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Цифровое производство',
                              reply_markup=markup)
    elif call.data == 'exhibition_2':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Металлообработка',
                              reply_markup=markup)
    elif call.data == 'exhibition_3':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Транспортное машиностроение',
                              reply_markup=markup)
    elif call.data == 'exhibition_4':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Технологии для городов',
                              reply_markup=markup)
    elif call.data == 'exhibition_5':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Промышленные IT',
                              reply_markup=markup)
    elif call.data == 'exhibition_6':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Технологии для энергетики',
                              reply_markup=markup)
    elif call.data == 'exhibition_7':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Новые материалы',
                              reply_markup=markup)
    elif call.data == 'exhibition_8':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Производство компонентов',
                              reply_markup=markup)
    elif call.data == 'exhibition_9':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Медицинская техника и оборудование для реабилитации',
                              reply_markup=markup)
    elif call.data == 'exhibition_10':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Автоматизация и робототехника',
                              reply_markup=markup)


@bot.callback_query_handler(func=lambda call: 'exhibitors' in call.data)
def exhibitors_submenu(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton('Назад', callback_data='to_back_exhibitors'), )

    if call.data == 'exhibitors_1':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='Рекламные и PR опции',
                              reply_markup=markup)

    elif call.data == 'exhibitors_2':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='АРЕНДА ПЕРЕГОВОРНОЙ КОМНАТЫ',
                              reply_markup=markup)

    elif call.data == 'exhibitors_3':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='ОХРАНА ВЫСТАВОЧНЫХ СТЕНДОВ',
                              reply_markup=markup)

    elif call.data == 'exhibitors_4':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text='ТРЕВЕЛ-СОПРОВОЖДЕНИЕ',
                              reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'tobook')
def tobook_submenu(call):
    text = 'Тут должна случиться магия, но у нас кончилась волшебная пыльца *('
    bot.answer_callback_query(call.id, text, show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data)
def invalid_request(call):
    text = 'Запрос не был выполнен, так как истёк срок его отправки или он был некорректно сформирован.'
    bot.answer_callback_query(call.id, text, show_alert=True)