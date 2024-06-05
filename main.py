from data.loader import bot
from utils.antiflood_middleware import SimpleMiddleware
from utils.is_admin_filter import IsAdmin

from handler import handler_com_admin, handler_com, handler_call


bot.add_custom_filter(IsAdmin())
# bot.setup_middleware(SimpleMiddleware(1))


if __name__ == '__main__':
    bot.polling(none_stop=True)

