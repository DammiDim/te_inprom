from data.loader import bot
from utils.is_admin_filter import IsAdmin

from handler import handler_com_admin, handler_com, handler_call
from utils.misc_func import name_later

bot.add_custom_filter(IsAdmin())

if __name__ == '__main__':
    name_later()
    bot.polling(none_stop=True, interval=1)

# Бот
# 1. Задать вопрос ! +

