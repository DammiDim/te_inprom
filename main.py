from data.loader import bot
from utils.antiflood_middleware import SimpleMiddleware
from utils.is_admin_filter import IsAdmin

from handler import handler_com_admin, handler_com, handler_call
from utils.misc_func import name_later

bot.add_custom_filter(IsAdmin())
# bot.setup_middleware(SimpleMiddleware(1))


if __name__ == '__main__':
    name_later()
    bot.polling(none_stop=True)

# Бот
# 1. Перерисовку клавиатуры (декоратор)
# 2. Гибкая возможность добавления админов
