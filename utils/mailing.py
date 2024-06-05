import telebot
from data import config

mail_bot = telebot.TeleBot(config.TOKEN)


def mailing_msg(chat_ids, current_chat_id, message_ids: list):
    for i in chat_ids:
        mail_bot.copy_messages(i, current_chat_id, message_ids)

