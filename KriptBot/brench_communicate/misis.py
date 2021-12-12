import random

import KriptBot.view.random_phrases as dialog
from KriptBot.view.menu import get_default_menu, button_menu

channel_id = "@ochki_zaychki"


# def check_sub_channel(chat_member):
#     if chat_member is None:
#         return False
#     return True


def stiker(message, bot):
    user_id = message.from_user.id
    try:
        flag = bot.get_chat_member(chat_id=-1001550334261, user_id=user_id)
    except:
        flag = False
    if flag.status != "left":
        bot.send_message(user_id, "Все прекрасно, вижу тебя)\nДержи классный стикерпак, так держать!\n\nА теперь...")
        bot.send_sticker(user_id, "CAACAgIAAxkBAAEDdvVhtRwV_0asD9vA0Er4zR5URI50UQACPxUAAuw1qUmw0gmusSURiyME")
        bot.send_message(user_id, "На самом деле я шучу, лучше оставайся с нами, так веселее ^_^",
                         reply_markup=get_default_menu())
    else:
        bot.send_message(user_id, "Хмм... Я тебя не вижу в подписчиках группы https://t.me/ochki_zaychki",
                         reply_markup=get_default_menu())



