from telebot import SimpleCustomFilter, types

from data.loader import mySql


class IsAdmin(SimpleCustomFilter):
    key = 'is_admin'
    _admins = mySql.get_all_admins_ids()

    def check(self, message: types.Message):
        return message.chat.id in self._admins
