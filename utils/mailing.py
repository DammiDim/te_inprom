import telebot
from telebot.apihelper import ApiTelegramException

from data import config
from time import sleep

from data.config import USER_STATUS_LOCKED
from database import quasi_db


def mailing_msg(chat_ids, current_chat_id, message_ids: list):
    _mail_bot = telebot.TeleBot(config.TOKEN)
    _my_sql3 = quasi_db.MySQL('inprom_users.db')

    for i in chat_ids:
        try:
            _mail_bot.copy_messages(i, current_chat_id, message_ids)
            sleep(0.1)
        except ApiTelegramException as e:
            _my_sql3.update_status(i, USER_STATUS_LOCKED)

