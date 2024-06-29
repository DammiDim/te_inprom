from data.loader import bot, set_new_com
from utils.is_admin_filter import IsAdmin

from handler import handler_com_admin, handler_com, handler_call

bot.add_custom_filter(IsAdmin())

if __name__ == '__main__':
    set_new_com()
    bot.polling(none_stop=True, interval=1)
