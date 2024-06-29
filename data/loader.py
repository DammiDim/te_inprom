import tracemalloc
from telebot import types
from telebot import TeleBot
from data import config

tracemalloc.start()
bot = TeleBot(config.TOKEN)


def set_new_com():
    bot.delete_my_commands(scope=None, language_code=None)

    bot.set_my_commands(
        commands=[
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Техподдержка"),
        ]
    )
