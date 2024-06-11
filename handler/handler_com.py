from telebot import types

from data.loader import bot
from database import quasi_db
from keyboard.inline.inline_button import register_btn, exhibitors_btn, dl_app_btn, address_btn, \
    vip_participation_btn, upcoming_projects_btn
from keyboard.replay.reply_button import welcome_btn
from data.texts import *
# from utils.misc_func import update_reply_keyboard


####################################################################################################
############################################# КОМАНДЫ ##############################################

@bot.message_handler(is_admin=False, commands=['start'])
def welcome(message):
    bot.clear_reply_handlers(message)

    telegram_id = message.chat.id
    username = message.from_user.username
    role = 0
    markup = welcome_btn()

    my_sql = quasi_db.MySQL('inprom_users.db')
    my_sql.add_user(telegram_id, username, role)

    bot.send_message(message.chat.id, t_welcome, reply_markup=markup)


####################################################################################################
###################################### ОБРАБОТЧИК СООБЩЕНИЙ ########################################

@bot.callback_query_handler(func=lambda call: call.data == 'to_back_exhibition')
@bot.message_handler(func=lambda message: message.text == 'О выставке')
def exhibition(message):
    if type(message) is types.Message:
        chat_id = message.chat.id
        bot.send_message(chat_id, t_exhibition)

    if type(message) is types.CallbackQuery:
        chat_id = message.message.chat.id
        message_id = message.message.message_id
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibition)


@bot.message_handler(func=lambda message: message.text == 'VIP участие')
def vip_participation(message):
    markup = vip_participation_btn()
    bot.send_message(message.chat.id, t_vip_participation, reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: call.data == 'to_back_register')
@bot.message_handler(func=lambda message: message.text == 'Регистрация')
def register(message):
    markup = register_btn()

    if type(message) is types.Message:
        bot.send_message(message.chat.id, t_register, reply_markup=markup)

    if type(message) is types.CallbackQuery:
        chat_id = message.message.chat.id
        message_id = message.message.message_id
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_register,
                              reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Ваше участие в 2025 году')
def to_book(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(text='Отправить запрос', callback_data='a'),
    )

    bot.send_message(message.chat.id, t_tobook, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Время работы выставки')
def times(message):
    bot.send_message(message.chat.id, t_times, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Как добраться')
def address(message):
    markup = address_btn()
    bot.send_message(message.chat.id, t_address, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Схема выставки')
def scheme(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(
            text='Открыть схему выставки',
            web_app=types.WebAppInfo(r'https://in.umap.world/reu')),
    )

    bot.send_message(message.chat.id, t_scheme, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Назначить встречу на выставке')
def make_appointment(message):
    markup = dl_app_btn()
    bot.send_message(message.chat.id, t_make_appointment, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Диалог с торгпредом')
def representative(message):
    markup = dl_app_btn()
    bot.send_message(message.chat.id, t_representative, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'ТОП-спикеры')
def spikes(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(text='Актуальный список будет позже, как пример',
                                   url='https://expo.innoprom.com/speakers/'),
    )

    bot.send_message(message.chat.id, 'ТОП-спикеры', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Деловая программа')
def business_program(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
        types.InlineKeyboardButton(text='Деловая программа',
                                   url='https://expo.innoprom.com/business-program/'),
    )
    bot.send_message(message.chat.id, 'Деловая программа доступна по кнопке ниже', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'to_back_exhibitors')
@bot.message_handler(func=lambda message: message.text == 'Экспонентам')
def exhibitors(message):
    markup = exhibitors_btn()

    if type(message) is types.Message:
        bot.send_message(message.chat.id, text=t_exhibitors, parse_mode='html', reply_markup=markup,disable_web_page_preview = True)

    if type(message) is types.CallbackQuery:
        chat_id = message.message.chat.id
        message_id = message.message.message_id
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_exhibitors,
                              reply_markup=markup,  parse_mode='html',disable_web_page_preview = True)


@bot.message_handler(func=lambda message: message.text == 'Контакты')
def contacts(message):
    bot.send_message(message.chat.id, t_contact)


@bot.callback_query_handler(func=lambda call: call.data == 'to_back_upcoming_proj')
@bot.message_handler(func=lambda message: message.text == 'Ближайшие проекты')
def upcoming_projects(message):
    markup = upcoming_projects_btn()
    if type(message) is types.Message:
        bot.send_message(message.chat.id, t_upcoming_proj, reply_markup=markup)

    if type(message) is types.CallbackQuery:
        chat_id = message.message.chat.id
        message_id = message.message.message_id
        bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                              text=t_upcoming_proj,
                              reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Организаторы')
def org(message):
    markup1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton('Подробнее', url=r'https://minpromtorg.gov.ru/'),
    )
    markup2 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton('Подробнее', url=r'https://midural.ru/'),
    )
    markup3 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton('Подробнее', url=r'https://business-event.com/'),
    )

    bot.send_message(message.chat.id, t_org_1, disable_web_page_preview=True, parse_mode='html', reply_markup=markup1)
    bot.send_message(message.chat.id, t_org_2, disable_web_page_preview=True, parse_mode='html', reply_markup=markup2)
    bot.send_message(message.chat.id, t_org_3, disable_web_page_preview=True, parse_mode='html', reply_markup=markup3)
