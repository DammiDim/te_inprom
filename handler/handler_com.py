from telebot import types

from data.loader import bot
from keyboard.inline.inline_button import exhibition_btn, register_btn, exhibitors_btn
from keyboard.replay.reply_button import welcome_btn
from data.texts import *


@bot.message_handler(commands=['start'])
def welcome(message):
    ID = message.chat.id
    first_name = message.from_user.first_name

    message_text = f'Привет {first_name}!\nВаш user ID: {ID}\n'

    markup = welcome_btn()
    bot.send_message(message.chat.id, message_text, parse_mode='Markdown', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'to_back_exhibition')
@bot.message_handler(func=lambda message: message.text == 'О выставке')
def exhibition(message):
    markup = exhibition_btn()
    if type(message) is types.Message:
        chat_id = message.chat.id
        bot.send_message(chat_id, t_exhibition, reply_markup=markup)

    if type(message) is types.CallbackQuery:
        chat_id = message.message.chat.id
        message_id = message.message.message_id
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibition,
                              reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Регистрация')
def register(message):
    markup = register_btn()

    bot.send_message(message.chat.id, 'Регистрация', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Забронировать площадь на 2025 год')
def to_book(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(text='Отправить запрос mailto:savin@innoprom.com', callback_data='tobook'),
    )

    bot.send_message(message.chat.id, t_tobook, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Схема выставки')
def scheme(message):
    bot.send_message(message.chat.id, 'It will be later')


@bot.message_handler(func=lambda message: message.text == 'Время работы выставки')
def times(message):
    bot.send_message(message.chat.id, t_times)


@bot.message_handler(func=lambda message: message.text == 'Деловая программа')
def business_program(message):
    bot.send_message(message.chat.id, 'It will be later')


@bot.message_handler(func=lambda message: message.text == 'ТОП-спикеры')
def spikes(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(text='Актуальный список будет позже, как пример',
                                   web_app=types.WebAppInfo('https://expo.innoprom.com/speakers/')),
    )

    bot.send_message(message.chat.id, 'ТОП-спикеры', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Назначить встречу на выставке')
def make_appointment(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(text='Наше приложение. Будет позже',
                                   callback_data='app'),
    )
    bot.send_message(message.chat.id, 'Назначайте деловые встречи с представителями из более чем 600 компаний, '
                                      'используя мобильное приложение INNOPROM', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Диалог с торгпредом')
def representative(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(text='Наше приложение. Будет позже',
                                   callback_data='app'),
    )
    bot.send_message(message.chat.id, t_representative, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Как добраться')
def address(message):
    bot.send_message(message.chat.id, t_address)
    bot.send_location(message.chat.id, 56.768099, 60.759315)


@bot.callback_query_handler(func=lambda call: call.data == 'to_back_exhibitors')
@bot.message_handler(func=lambda message: message.text == 'Экспонентам')
def exhibitors(message):
    markup = exhibitors_btn()
    text = 'Сделайте ваше участие комфортнее и эффективнее, используя полезные сервисы наших партнеров.'
    if type(message) is types.Message:
        bot.send_message(message.chat.id, text=text, reply_markup=markup)

    if type(message) is types.CallbackQuery:
        chat_id = message.message.chat.id
        message_id = message.message.message_id
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=text,
                              reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Контакты')
def contacts(message):
    bot.send_message(message.chat.id, t_contact)


@bot.message_handler(func=lambda message: message.text == 'Ближайшие проекты')
def upcoming_projects(message):
    bot.send_message(message.chat.id, t_proj)


@bot.message_handler(func=lambda message: message.text == 'Организаторы')
def org(message):
    bot.send_message(message.chat.id, t_org)


@bot.message_handler(content_types=['text'])
def mess(message):
    bot.send_message(message.chat.id, f'У меня нет такой команды..но я еще учусь!', parse_mode='Markdown')
