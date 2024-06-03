from pprint import pprint

import telebot

from data import config
from database import quasi_db

bot = telebot.TeleBot(config.TOKEN, use_class_middlewares=True)


bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("start", "Запускает бота"),
    ]
)

mySql = quasi_db.MySQL('inprom_users.db')

userss = mySql.get_all_users()
pprint(userss)

userss = mySql.get_all_admins()
pprint(userss)

