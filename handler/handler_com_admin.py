from telebot import types
import pandas as pd

from data.config import DATABASE_NAME
from data.loader import bot
from data.texts import t_welcome
from database.sql_db import SqlDB
from keyboard.replay.reply_button import welcome_btn
from utils.mailing import start_mailing, mailing_msg, get_selection_msg

_msg_ids = []
_check = 0


@bot.message_handler(is_admin=True, commands=['start'])
def welcome(message):
    bot.clear_reply_handlers(message)
    markup = welcome_btn()

    markup.add(
        types.KeyboardButton('❗ Отправить сообщение всем ❗'),
        types.KeyboardButton('❗ Выгрузить базу ❗'),
        types.KeyboardButton('❗ Проверить очередь ❗'),
    )

    bot.send_message(message.chat.id, t_welcome, reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text == '❗ Проверить очередь ❗', is_admin=True)
def message_everyone(message):

    _chat_id = message.chat.id
    _message_id = message.message_id

    mailing_msg(_chat_id, 20)


@bot.message_handler(
    func=lambda message: message.text in [
        '❗ Отправить сообщение всем ❗',
        'Отправить сообщение 🟢',
        'Нет, отправить новые 🔴'],
    is_admin=True)
def message_everyone(message):
    global _check, _msg_ids
    _check = 1
    _msg_ids = []

    chat_id = message.chat.id
    message_id = message.id
    _markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    _markup.add(
        types.KeyboardButton('Главное меню 🟡'),
        types.KeyboardButton('Готово 🟢'))

    _text = '❗ <b><i>Отправьте сообщения для рассылки и нажмите "Готово"</i></b>'

    bot.delete_message(chat_id, message_id)
    bot.send_message(chat_id, _text, reply_markup=_markup, parse_mode='html')


@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Готово 🟢')
def message_everyone(message):
    global _msg_ids, _check
    _check = 0

    _markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    _text = ''

    if not _msg_ids:
        _markup.add(
            types.KeyboardButton(text='Главное меню 🟡'),
            types.KeyboardButton(text='Отправить сообщение 🟢'),
        )
        _text = ('❗ <b><i>Возникла проблема с отправкой ваших сообщений. Пожалуйста, '
                 'проверьте, всё ли заполнено верно, и попробуйте ещё раз.</i></b>')
    else:
        _markup.add(
            types.KeyboardButton(text='Да, все верно 🟢'),
            types.KeyboardButton(text='Нет, отправить новые 🔴'),
        )
        _markup.add(types.KeyboardButton(text='Главное меню 🟡'), )
        _text = '❗ <b><i>Проверьте и подтвердите отправку.</i></b>'

    bot.send_message(message.chat.id, _text, reply_markup=_markup, parse_mode='html')


@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Да, все верно 🟢')
def dispatch_msg(message):
    global _msg_ids
    _chat_id = message.chat.id
    _message_id = message.message_id
    _markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    _markup.add(types.KeyboardButton('Главное меню 🟡'))

    bot.send_message(chat_id=_chat_id,
                     text='<b><i>Отправка началась</i></b> 🟡',
                     reply_markup=_markup,
                     parse_mode='html')

    start_mailing(_chat_id, _msg_ids)

    bot.send_message(chat_id=_chat_id,
                     text='<b><i>Сообщение было отправлено</i></b> ✅',
                     parse_mode='html')


@bot.message_handler(is_admin=True, func=lambda message: message.text in ['Главное меню 🟡'])
def back_mainmenu(message):
    chat_id = message.chat.id
    message_id = message.id

    markup = welcome_btn()
    markup.add(
        types.KeyboardButton('❗ Отправить сообщение всем ❗'),
        types.KeyboardButton('❗ Выгрузить базу ❗'),
        types.KeyboardButton('❗ Проверить очередь ❗'),
    )

    bot.delete_message(chat_id, message_id)
    bot.send_message(chat_id, 'Вы вернулись в меню', reply_markup=markup)


@bot.message_handler(is_admin=True, func=lambda message: message.text == '❗ Выгрузить базу ❗')
def cmd_export(message):
    _sqlDB = SqlDB(f"{DATABASE_NAME}")
    _data = _sqlDB.select("SELECT telegram_id, username, status FROM users")
    _df = pd.DataFrame(_data)
    _df.to_excel('database/output.xlsx', index=True, header=True)
    _file = open('database/output.xlsx', 'rb')
    bot.send_document(message.chat.id, document=_file)


@bot.message_handler(is_admin=True, func=lambda message: message.text)
def cmd_export(message):
    global _msg_ids, _check
    _chat_id = message.chat.id
    _message_id = message.message_id

    if _check == 1:
        _msg_ids.append(_message_id)
