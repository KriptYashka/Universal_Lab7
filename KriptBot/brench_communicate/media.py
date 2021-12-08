import os
import random
import KriptBot.view.random_phrases as dialog
from KriptBot.view.menu import get_default_menu


def send_photo(message, bot):
    user_id = message.from_user.id
    bot.send_message(user_id, dialog.send_photo(), reply_markup=get_default_menu())
    path = os.path.normpath(os.getcwd() + os.sep + os.pardir + os.path.join("/KriptBot/media/photo"))
    res = random.choice(os.listdir(path))
    p = os.path.join(path, res)
    photo = open(p, "rb")
    bot.send_photo(user_id, photo)

