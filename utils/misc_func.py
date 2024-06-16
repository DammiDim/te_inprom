from data.config import ADMINS, TECHNICAL_SUPPORT, ADMIN_ROLE
from data.loader import bot, mySql
from telebot import types

from keyboard.replay.reply_button import welcome_btn


# todo come up with a name
def name_later():
    _admin = [ADMINS,]
    _technical_suppopt = [TECHNICAL_SUPPORT,]

    _bd_admins = mySql.get_all_admins_ids()
    _bd_users = mySql.get_all_users_ids()
    _new_list = list(set(_admin).difference(_bd_admins))

    for i in _new_list:
        mySql.add_user(i, f'innprom admin', ADMIN_ROLE)

    _new_list = list(set(_admin).difference(_bd_users))
    for i in _new_list:
        mySql.update_role(i, ADMIN_ROLE)

