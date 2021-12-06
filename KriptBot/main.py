import telebot
import re
from view.menu import get_default_menu
from view.commands import classic_cmd

token = "5052598391:AAEkznKpNqmh2dmy9HehEpOBjGIsGqSG3fg"  # Не смейте трогать моего бота! Меняйте токен
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def start_command(message):
    text = "Приветствую тебя, <b>{}</b>!".format(message.from_user.username)
    bot.send_message(message.from_user.id, text, parse_mode="HTML")
    bot.send_photo(message.from_user.id, 'https://i.pinimg.com/474x/2f/16/02/2f1602f14b24dc574bb76cd512ebc24e--black'
                                         '-kittens-warrior-cats.jpg')
    text = "Чем сегодня займемся? =)"
    bot.send_message(message.from_user.id, text, parse_mode="HTML", reply_markup=get_default_menu())

@bot.message_handler(func=lambda message: True)
def listen_message(message):
    text = message.text.lower()

    #  Определение команд для пользователя

    types_user = [None]

    actions = classic_cmd
    for regular, action in actions.items():
        if re.search(regular):
            action(message, bot)
            return

    bot.send_message(message.from_user.id, random_text.dont_know(), reply_markup=get_default_menu(message.from_user.id))


def main():
    print("Бот запущен")
    bot.polling()


if __name__ == '__main__':
    main()