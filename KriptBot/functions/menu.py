import telebot


def get_menu():
    menu = telebot.types.ReplyKeyboardMarkup()

    params = ["Привет", "Как дела?", "Расскажи анекдот", ["Погода завтра", "Погода сегодня"]]

    for item in params:
        if isinstance(item, list):
            menu.add(*item)
        else:
            menu.add(item)
    return menu