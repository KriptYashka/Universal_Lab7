import telebot
import KriptBot.view.random_phrases as dialog
from KriptBot.view.menu import get_default_menu


def send_hello(message, bot):
    user_id = message.from_user.id
    bot.send_message(user_id, dialog.hello(message.from_user.username), reply_markup=get_default_menu())


def send_how_are_you(message, bot):
    user_id = message.from_user.id
    bot.send_message(user_id, dialog.how_are_you(), reply_markup=get_default_menu())


def send_joke(message, bot):
    user_id = message.from_user.id
    bot.send_message(user_id, dialog.joke(), reply_markup=get_default_menu())
