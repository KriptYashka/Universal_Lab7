import telebot
from functions.menu import get_menu
from functions import random_phrases as dialog

token = ""  # Токен на твоего бота, взять его можно с помощью @BotFather
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def start_command(message):
    text = "Приветствую тебя, <b>{}</b>!".format(message.from_user.username)
    bot.send_message(message.from_user.id, text, parse_mode="HTML")


@bot.message_handler(func=lambda message: True)
def listen_text_message(message):
    cmd = message.text.lower()

    #  Определение команд для пользователя

    if cmd.count("привет"):
        bot.send_message(message.from_user.id, dialog.hello(message.from_user.username), reply_markup=get_menu())
    elif cmd.count("как дела"):
        bot.send_message(message.from_user.id, dialog.how_are_you(), reply_markup=get_menu())
    elif cmd.count("погода") and cmd.count("завтра"):
        bot.send_message(message.from_user.id, dialog.tomorrow_weather(), reply_markup=get_menu())
    elif cmd.count("погода") and cmd.count("сегодня"):
        bot.send_message(message.from_user.id, dialog.today_weather(), reply_markup=get_menu())
    elif cmd.count("анекдот"):
        bot.send_message(message.from_user.id, dialog.joke(), reply_markup=get_menu())
    else:
        bot.send_message(message.from_user.id, dialog.dont_know(), reply_markup=get_menu())


@bot.message_handler(content_types=["photo", "sticker", "audio"])
def listen_photo_message(message):
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEDeAFhtixIeauKA_p3zfPWWvF_eRfgFAACOQMAArVx2gYjUGZnvEY4rSME"
                     , reply_markup=get_menu())


def main():
    print("Бот запущен")
    bot.polling()


if __name__ == '__main__':
    main()
