from telebot import types

from data.loader import bot
from data.texts import t_welcome
from database import quasi_db
from keyboard.replay.reply_button import welcome_btn
from utils.mailing import mailing_msg

_msg_ids = []
_msg_start_id = 0


@bot.message_handler(is_admin=True, commands=['start'])
def welcome(message):
    bot.clear_reply_handlers(message)

    markup = welcome_btn()

    btn1 = types.KeyboardButton('❗ Отправить сообщение всем ❗')
    markup.add(btn1)

    bot.send_message(message.chat.id, t_welcome, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'back_to_message_everyone')
@bot.message_handler(is_admin=True, func=lambda message: message.text == '❗ Отправить сообщение всем ❗')
def message_everyone(message):
    global _msg_start_id
    _text = 'Отправьте сообщения для рассылки и нажмите "Готово"'

    if type(message) is types.Message:
        _msg_start_id = message.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton(text='Главное меню'),
            types.KeyboardButton('Готово'))
        bot.send_message(message.chat.id, _text, reply_markup=markup)

    if type(message) is types.CallbackQuery:
        chat_id = message.message.chat.id
        message_id = message.message.message_id
        _msg_start_id = message_id-1
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=_text)


@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Готово')
def message_everyone(message):
    global _msg_ids, _msg_start_id
    _collect_ids = []

    for i in range(_msg_start_id+2, message.id):
        _collect_ids.append(i)
    _msg_ids = _collect_ids

    _markup = types.InlineKeyboardMarkup(row_width=1)
    _text = ''
    if not _msg_ids:
        _markup.add(
            types.InlineKeyboardButton(text='Отправить сообщение 🟢', callback_data='back_to_message_everyone'),
            types.InlineKeyboardButton(text='Главное меню 🔴', callback_data='back_to_menu'),
        )
        _text = 'Сообщения не могут быть отправлены, так как они отсутствуют.'

    else:
        _markup.add(
            types.InlineKeyboardButton(text='Да, все верно 🟢', callback_data='dispatch'),
            types.InlineKeyboardButton(text='Нет, отправить новые 🔴', callback_data='back_to_message_everyone'),
        )
        _text = 'Проверьте и подтвердите отправку.'

    bot.send_message(message.chat.id, _text, reply_markup=_markup)


@bot.callback_query_handler(func=lambda call: call.data == 'dispatch')
def exhibitors_submenu(call):
    global _msg_ids

    my_sql = quasi_db.MySQL('inprom_users.db')
    users = my_sql.get_all_users_ids()

    chat_id = call.message.chat.id
    message_id = call.message.message_id

    mailing_msg(users, chat_id, _msg_ids)

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text='Главное меню', callback_data='back_to_menu'),
    )
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Сообщение было отправлено ✅', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'back_to_menu')
@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Главное меню')
def exhibitors_submenu(message):
    chat_id = message.chat.id
    message_id = message.id
    if type(message) is types.CallbackQuery:
        chat_id = message.message.chat.id
        message_id = message.message.message_id

    markup = welcome_btn()
    markup.add(types.KeyboardButton('❗ Отправить сообщение всем ❗'))

    bot.delete_message(chat_id, message_id)
    bot.send_message(chat_id, 'Вы вернулись в меню', reply_markup=markup)
    