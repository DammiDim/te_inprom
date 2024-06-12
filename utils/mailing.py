import telebot
from data import config
from time import sleep

def mailing_msg(chat_ids, current_chat_id, message_ids: list):
    mail_bot = telebot.TeleBot(config.TOKEN)

    for i in chat_ids:
        mail_bot.copy_messages(i, current_chat_id, message_ids)
        sleep(0.1)
