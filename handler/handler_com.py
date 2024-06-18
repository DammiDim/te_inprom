from telebot import types
from telebot.types import InputMediaPhoto

from data.config import TECHNICAL_SUPPORT, USER_ROLE
from data.loader import bot
from database import quasi_db
from keyboard.inline.inline_button import *
from keyboard.replay.reply_button import welcome_btn
from data.texts import *


# from utils.misc_func import update_reply_keyboard


####################################################################################################
############################################# КОМАНДЫ ##############################################


@bot.message_handler(is_admin=False, commands=['start'])
def welcome(message):
    bot.clear_reply_handlers(message)

    _telegram_id = message.chat.id
    _username = message.from_user.username
    _role = USER_ROLE
    _markup = welcome_btn()

    _my_sql = quasi_db.MySQL('inprom_users.db')
    _my_sql.add_user(_telegram_id, _username, _role)

    bot.send_message(message.chat.id, t_welcome, reply_markup=_markup)


####################################################################################################
###################################### ОБРАБОТЧИК СООБЩЕНИЙ ########################################


@bot.message_handler(func=lambda message: message.text == 'О выставке')
def exhibition(message):
    _chat_id = message.chat.id
    _photo = open('img/img_exhibition.png', 'rb')

    bot.send_photo(_chat_id, photo=_photo, caption=t_exhibition)


@bot.message_handler(func=lambda message: message.text == 'VIP участие')
def vip_participation(message):
    _chat_id = message.chat.id
    _photo = open('img/img_vip_participation.png', 'rb')
    _markup = vip_participation_btn()

    bot.send_photo(_chat_id, photo=_photo, caption=t_vip_participation, reply_markup=_markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: call.data == 'to_back_register')
@bot.message_handler(func=lambda message: message.text == 'Регистрация')
def register(message):
    _photo = open('img/img_register.png', 'rb')
    _markup = register_btn()

    if type(message) is types.Message:
        _chat_id = message.chat.id
        bot.send_photo(_chat_id, photo=_photo, caption=t_register, reply_markup=_markup, parse_mode='html')

    if type(message) is types.CallbackQuery:
        _chat_id = message.message.chat.id
        _message_id = message.message.message_id
        _media = InputMediaPhoto(media=_photo, caption=t_register, parse_mode='html')
        bot.edit_message_media(media=_media,
                               chat_id=_chat_id,
                               message_id=_message_id,
                               reply_markup=_markup)


@bot.message_handler(func=lambda message: message.text == 'Ваше участие в 2025 году')
def to_book(message):
    _chat_id = message.chat.id
    _photo = open('img/img_to_book.png', 'rb')
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton(text='Отправить запрос', url=r'https://tinyurl.com/2ssspycc'),
    )

    bot.send_photo(_chat_id, photo=_photo, caption=t_tobook, reply_markup=_markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Время работы выставки')
def times(message):
    _chat_id = message.chat.id
    _photo = open('img/img_times.png', 'rb')

    bot.send_photo(_chat_id, photo=_photo, caption=t_times, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Как добраться')
def address(message):
    _chat_id = message.chat.id
    _photo = open('img/img_address.png', 'rb')
    _markup = address_btn()

    bot.send_photo(_chat_id, photo=_photo, caption=t_address, reply_markup=_markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Схема выставки')
def scheme(message):
    _chat_id = message.chat.id
    _photo = open('img/img_scheme.png', 'rb')
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton(
            text='Открыть схему выставки',
            web_app=types.WebAppInfo(r'https://in.umap.world/reu')),
    )

    bot.send_photo(_chat_id, photo=_photo, caption=t_scheme, reply_markup=_markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Назначить встречу на выставке')
def make_appointment(message):
    _chat_id = message.chat.id
    _photo = open('img/img_make_appointment.png', 'rb')
    _markup = dl_app_btn()

    bot.send_photo(_chat_id, photo=_photo, caption=t_make_appointment, reply_markup=_markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Диалог с торгпредом')
def representative(message):
    _chat_id = message.chat.id
    _photo = open('img/img_representative.png', 'rb')
    _markup = dl_app_btn()

    bot.send_photo(_chat_id, photo=_photo, caption=t_representative, reply_markup=_markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'ТОП-спикеры')
def spikes(message):
    _chat_id = message.chat.id
    _photo = open('img/img_representative.png', 'rb')
    _markup = spikes_btn()

    bot.send_photo(_chat_id, photo=_photo, caption='ТОП-спикеры', reply_markup=_markup, parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'Деловая программа')
def business_program(message):
    _chat_id = message.chat.id
    _photo = open('img/img_business_program.png', 'rb')
    _markup = business_program_btn()

    bot.send_photo(_chat_id, photo=_photo,
                   caption='<i>Деловая программа доступна по кнопке ниже</i>',
                   reply_markup=_markup,
                   parse_mode='html')


@bot.callback_query_handler(func=lambda call: call.data == 'to_back_exhibitors')
@bot.message_handler(func=lambda message: message.text == 'Экспонентам')
def exhibitors(message):
    _markup = exhibitors_btn()
    _photo = open('img/img_exhibitors.png', 'rb')

    if type(message) is types.Message:
        _chat_id = message.chat.id
        bot.send_photo(chat_id=_chat_id,
                       photo=_photo,
                       caption=t_exhibitors,
                       reply_markup=_markup,
                       parse_mode='html', )

    if type(message) is types.CallbackQuery:
        _chat_id = message.message.chat.id
        _message_id = message.message.message_id
        _media = InputMediaPhoto(media=_photo, caption=t_exhibitors, parse_mode='html')
        bot.edit_message_media(media=_media,
                               chat_id=_chat_id,
                               message_id=_message_id,
                               reply_markup=_markup)


@bot.message_handler(func=lambda message: message.text == 'Контакты')
def contacts(message):
    _chat_id = message.chat.id
    _photo = open('img/img_contacts.png', 'rb')
    _markup = types.InlineKeyboardMarkup(row_width=1)
    _markup.add(
        types.InlineKeyboardButton(
            text='Контакты',
            url=r'https://expo.innoprom.com/contacts/team/'), )

    bot.send_photo(_chat_id, photo=_photo, caption=t_contact, reply_markup=_markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: call.data == 'to_back_upcoming_proj')
@bot.message_handler(func=lambda message: message.text == 'Ближайшие проекты')
def upcoming_projects(message):
    _photo = open('img/img_upcoming_projects.png', 'rb')
    _markup = upcoming_projects_btn()

    if type(message) is types.Message:
        _chat_id = message.chat.id
        bot.send_photo(chat_id=_chat_id,
                       photo=_photo,
                       caption=t_upcoming_proj,
                       reply_markup=_markup,
                       parse_mode='html')

    if type(message) is types.CallbackQuery:
        _chat_id = message.message.chat.id
        _message_id = message.message.message_id
        _media = InputMediaPhoto(media=_photo, caption=t_upcoming_proj, parse_mode='html')
        bot.edit_message_media(media=_media,
                               chat_id=_chat_id,
                               message_id=_message_id,
                               reply_markup=_markup)


@bot.message_handler(func=lambda message: message.text == 'Организаторы')
def organizers(message):
    _chat_id = message.chat.id
    _photo = open('img/img_organizers.png', 'rb')
    _markup = organizers_btn()
    _markup_be = types.InlineKeyboardMarkup(row_width=1)
    _markup_be.add(
        types.InlineKeyboardButton(
            text='Business Event',
            url=r'https://business-event.com/ '), )

    bot.send_photo(_chat_id, photo=_photo, caption='<i>Информация об организаторах</i>',
                   reply_markup=_markup, parse_mode='html')
    bot.send_message(_chat_id, t_organizers, reply_markup=_markup_be)
