from telebot import SimpleCustomFilter, types

from data.config import ADMINS


class IsAdmin(SimpleCustomFilter):
    key = 'is_admin'

    def check(self, message: types.Message):
        return message.chat.id in ADMINS

