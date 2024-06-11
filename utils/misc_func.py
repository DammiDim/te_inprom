from data.config import ADMINS
from data.loader import bot, mySql
from telebot import types

from keyboard.replay.reply_button import welcome_btn


# todo come up with a name
def name_later():
    list_admins = ADMINS
    bd_admins = mySql.get_all_admins_ids()
    bd_users = mySql.get_all_users_ids()
    new_list = list(set(list_admins).difference(bd_admins))
    for i in new_list:
        mySql.add_user(i, f'u_{i}', 1)

    new_list = list(set(list_admins).difference(bd_users))
    for i in new_list:
        mySql.update_role(i, 1)

