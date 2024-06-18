from telebot import types

from data.config import TECHNICAL_SUPPORT
from data.loader import bot
from keyboard.inline.inline_button import *
from keyboard.replay.reply_button import welcome_btn

_msg_id = 0


@bot.message_handler(commands=["help"])
@bot.message_handler(func=lambda message: message.text == '🔸 Задать вопрос 🔸')
def ask_question(message):
    global _msg_id
    _msg_id = message.id
    _markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    _markup.add(
        types.KeyboardButton('Главное меню'),)

    msg = bot.send_message(
        message.chat.id,
        '<b><i>Напишите свой вопрос боту <u>одним сообщением</u>.\nСкоро вам ответит команда техподдержки.</i></b>',
        reply_markup=_markup, parse_mode='html')

    bot.register_next_step_handler(msg, send_reply)


def send_reply(message):
    _chat_id = message.chat.id

    _markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    _markup.add(
        types.KeyboardButton('Главное меню'),
        types.KeyboardButton('Отправить вопрос'),
    )

    if message.text == 'Главное меню':
        _markup = welcome_btn()
        bot.send_message(_chat_id, '<b><i>Сообщение <u>не было отправлено</u>, вы вернулись в главное меню.</i></b>',
                         reply_markup=_markup, parse_mode='html')
    else:
        bot.send_message(_chat_id, '<b><i>Проверти и подтвердите отправку.</i></b>',
                         reply_markup=_markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Отправить вопрос')
def ask_question(message):
    global _msg_id

    _chat_id = message.chat.id
    _markup = welcome_btn()

    for _id in TECHNICAL_SUPPORT:
        bot.forward_message(_id, _chat_id, _msg_id + 2)
    bot.send_message(_chat_id, '<b><i>Сообщение было доставлено, ожидайте ответа.</i></b>',
                     reply_markup=_markup, parse_mode='html')


@bot.message_handler(content_types='text')
def handle_text(message):
    global _msg_id
    _chat_id = message.chat.id
    _markup = welcome_btn()

    if message.text == 'Отправить вопрос':
        for _id in TECHNICAL_SUPPORT:
            bot.forward_message(_id, _chat_id, _msg_id + 2)

        bot.send_message(_chat_id, '<b><i>Сообщение было доставлено, ожидайте ответа.</i></b>',
                         reply_markup=_markup, parse_mode='html')

    if message.text == 'Главное меню':
        bot.send_message(_chat_id, '<b><i>Сообщение <u>не было отправлено</u>, вы вернулись в главное меню.</i></b>',
                         reply_markup=_markup, parse_mode='html')

    if int(message.chat.id) in TECHNICAL_SUPPORT:
        try:
            help_user_id = message.reply_to_message.forward_from.id
            bot.send_message(help_user_id,
                             f'<b><i>Команда поддержки ответила на ваш вопрос.</i></b>\n\n{message.text}',
                             parse_mode='html')
        except Exception:
            pass
