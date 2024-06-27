from telebot import types
import pandas as pd

from data.loader import bot, mySql
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

    markup.add(
        types.KeyboardButton('❗ Отправить сообщение всем ❗'),
        types.KeyboardButton('❗ Выгрузить базу ❗'),
    )

    bot.send_message(message.chat.id, t_welcome, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'back_to_message_everyone')
@bot.message_handler(is_admin=True, func=lambda message: message.text == '❗ Отправить сообщение всем ❗')
def message_everyone(message):
    global _msg_start_id

    _text = 'Отправьте сообщения для рассылки и нажмите "Готово"'

    if type(message) is types.Message:
        _msg_start_id = message.id
        _markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        _markup.add(
            types.KeyboardButton('Главное меню'),
            types.KeyboardButton('Готово'))

        bot.send_message(message.chat.id, _text, reply_markup=_markup)

    if type(message) is types.CallbackQuery:
        chat_id = message.message.chat.id
        message_id = message.message.message_id
        _msg_start_id = message_id - 1

        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=_text)


@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Готово')
def message_everyone(message):
    global _msg_ids, _msg_start_id
    _msg_ids = [i for i in range(_msg_start_id + 2, message.id)]
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _text = ''

    if not _msg_ids:
        _markup.add(
            types.InlineKeyboardButton(text='Отправить сообщение 🟢', callback_data='back_to_message_everyone'),
            types.InlineKeyboardButton(text='Главное меню 🟡', callback_data='back_to_menu'),
        )
        _text = ('Возникла проблема с отправкой ваших сообщений. Пожалуйста, '
                 'проверьте, всё ли заполнено верно, и попробуйте ещё раз.')
    else:
        _markup.add(
            types.InlineKeyboardButton(text='Да, все верно 🟢', callback_data='dispatch'),
            types.InlineKeyboardButton(text='Нет, отправить новые 🔴', callback_data='back_to_message_everyone'),
        )
        _text = 'Проверьте и подтвердите отправку.'

    bot.send_message(message.chat.id, _text, reply_markup=_markup)


@bot.callback_query_handler(func=lambda call: call.data == 'dispatch')
def dispatch_msg(call):
    global _msg_ids
    _chat_id = call.message.chat.id
    _message_id = call.message.message_id

    _markup = welcome_btn()
    _markup.add(
        types.KeyboardButton('❗ Отправить сообщение всем ❗'),
        types.KeyboardButton('❗ Выгрузить базу ❗'),
    )

    mailing_msg(_chat_id, _msg_ids)
    bot.register_next_step_handler(call.message, exhibitors_submenu)
    bot.delete_message(_chat_id, _message_id)
    bot.send_message(chat_id=_chat_id, text='Сообщение было отправлено ✅', reply_markup=_markup)


@bot.callback_query_handler(func=lambda call: call.data == 'back_to_menu')
@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Главное меню')
def exhibitors_submenu(message):
    global _msg_ids, _msg_start_id
    _msg_ids = []
    _msg_start_id = 0

    if type(message) is types.CallbackQuery:
        chat_id = message.message.chat.id
        message_id = message.message.message_id
    else:
        chat_id = message.chat.id
        message_id = message.id

    markup = welcome_btn()
    markup.add(
        types.KeyboardButton('❗ Отправить сообщение всем ❗'),
        types.KeyboardButton('❗ Выгрузить базу ❗'),
    )

    bot.delete_message(chat_id, message_id)
    bot.send_message(chat_id, 'Вы вернулись в меню', reply_markup=markup)

    if type(message) is types.CallbackQuery:
        bot.answer_callback_query(message.id, text="")


@bot.message_handler(is_admin=True, func=lambda message: message.text == '❗ Выгрузить базу ❗')
def cmd_export(message):
    my_sql = quasi_db.MySQL('inprom_users.db')
    data = my_sql.get_all_records()
    df = pd.DataFrame(data)
    df.to_excel('database/output.xlsx', index=False, header=True)
    file = open('database/output.xlsx', 'rb')
    bot.send_document(message.chat.id, document=file)
