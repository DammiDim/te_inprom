from telebot import types

from data.loader import bot
from keyboard.replay.reply_button import welcome_btn


@bot.message_handler(is_admin=True, commands=['start'])
def welcome(message):
    bot.clear_reply_handlers(message)

    ID = message.chat.id
    first_name = message.from_user.first_name
    markup = welcome_btn()
    btn1 = types.KeyboardButton('Отправить сообщение всем')
    markup.add(btn1)

    message_text = f'Привет {first_name}!\nВаш user ID: {ID}\nYou admin'

    bot.send_message(message.chat.id, message_text, reply_markup=markup)


@bot.message_handler(is_admin=True, func=lambda message: message.text == 'Отправить сообщение всем')
def org(message):
    bot.send_message(message.chat.id, 'ok')
