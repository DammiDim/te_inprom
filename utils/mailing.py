import json
from datetime import datetime

from telebot import TeleBot
from telebot.apihelper import ApiTelegramException
from data import config
from time import sleep

from data.config import USER_STATUS_LOCKED, DATABASE_NAME
from database.sql_db import SqlDB


def msg_to_db(message_ids: list):
    _sqlDB = SqlDB(f"{DATABASE_NAME}")
    _tmp = _sqlDB.select("SELECT telegram_id FROM users WHERE status = ?", [1])
    _chat_ids = [i.get('telegram_id') for i in _tmp]

    tmp = json.dumps(message_ids)

    for user_id in _chat_ids:
        current_datetime = f'{datetime.now()} '

        _sqlDB.iud("INSERT INTO msg_queue (msg_ids, chat_id, date, status) VALUES (?, ?, ?, ?)",
                   (tmp, user_id, current_datetime, 0))


def get_selection_msg(limit):
    _sqlDB = SqlDB(f"{DATABASE_NAME}")
    _tmp = _sqlDB.select("SELECT * FROM msg_queue WHERE status = ? ORDER BY RANDOM() limit  ?",
                         (0, limit))
    return _tmp


def mailing_msg(current_chat_id, limit):
    _mail_bot = TeleBot(config.TOKEN)
    _sqlDB = SqlDB(f"{DATABASE_NAME}")
    _msgs = get_selection_msg(limit)

    while _msgs:
        for i in _msgs:
            try:
                _message_ids = json.loads(i['msg_ids'])
                _telegram_id = i['chat_id']
                _chat_id = i['chat_id']
                _date = i['date']

                _sqlDB.iud("UPDATE msg_queue SET status = ? WHERE date = ?",
                           (1, _date))
                _mail_bot.copy_messages(_chat_id, current_chat_id, _message_ids)

                _msgs.remove(i)
                sleep(0.05)

            except ApiTelegramException as e:
                if 'USER_IS_BLOCKED' in e.description:
                    _sqlDB.iud("UPDATE users SET status = ? WHERE telegram_id = ?",
                               (USER_STATUS_LOCKED, _telegram_id))

        _msgs = get_selection_msg(limit)


def start_mailing(current_chat_id, msg_ids):
    msg_to_db(msg_ids)
    mailing_msg(current_chat_id, 20)
