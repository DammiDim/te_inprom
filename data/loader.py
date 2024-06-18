import tracemalloc

import telebot
from data import config
from database import quasi_db

tracemalloc.start()
bot = telebot.TeleBot(config.TOKEN, use_class_middlewares=True)


bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("start", "Запустить бота"),
        telebot.types.BotCommand("help", "Техподдержка"),
    ]
)

mySql = quasi_db.MySQL('inprom_users.db')
