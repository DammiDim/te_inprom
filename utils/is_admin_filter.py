from telebot import types
from telebot import SimpleCustomFilter

from data.config import DATABASE_NAME, ADMIN_ROLE
from database.sql_db import SqlDB


class IsAdmin(SimpleCustomFilter):
    key = 'is_admin'

    _sqlDB = SqlDB(f"{DATABASE_NAME}")
    _tmp = _sqlDB.select("SELECT telegram_id FROM users WHERE role = ?", [ADMIN_ROLE])
    _admins = [i.get('telegram_id') for i in _tmp]
    print(_admins)

    def check(self, message: types.Message):
        return message.chat.id in self._admins
