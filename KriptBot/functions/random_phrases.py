import random
import KriptBot.functions.weather as weather
import KriptBot.functions.anecdot as anektod














""" Саня, поменяй фразы!!! """

















def hello(name=None):
    if name is not None:
        name = ", " + name
    text = [f"Приветик{name}! Очень рада, что у тебя появилось свободное время поговорить со мной😊",
            f"Мя-я-я-у! И тебе привет!",
            f"О{name}, как раз вспоминала о тебе, приветик☺️"]
    return random.choice(text)


def dont_know():
    text = ["Я знаю только 2 языка: человечий и кошачий. ",
            "Мяу? Это ещё что такое?",
            "Хм... Даже не знаю, как на это ответить🤔",
            "Может ты случайно уснул на клавиатуре? Я не совсем поняла тебя."]
    return random.choice(text)


def how_are_you():
    text = ["Все хорошо, спасибо) Надеюсь, что у тебя тоже😊",
            "Всю ночь тыгыдыкала, теперь отдыхаю.",
            "Прекрасно! Сегодня же всемирный день кошек, не знал?\nДа ладно, это я тебя разыгрываю😄"]
    temp_today = weather.get_weather_average()
    if temp_today < -10:
        text.append("Сегодня пролежала дома, вообще на улицу в такой дубак не хочется гулять, бррр...🥶")
        text.append("Я залипла на снег, не мешай.")
        text.append(f"Вышла на балкон и поняла, что при {temp_today:.1f} больше на балкон не хочется выходить. "
                    "Даже молоко в миске замерзло!")
    elif temp_today < 0:
        text.append("Сделала себе горячее молоко с ")
        text.append("В такую погоду стараюсь спать около батарей.")
        text.append(f"Прохладно сегодня было. На улице {temp_today:.1f}, поэтому рыбку из пруда достать не удалось(")
    elif temp_today < 10:
        text.append(f"Смотрела на лужи, в отражении видела что-то милое, прекрасное и очень зеленое💚")
    elif temp_today < 20:
        text.append(f"Прошлась по своей улице, в пруду нашла свою любимую рыбку, когда-нибудь я обязательно"
                    f" познакомлюсь с ней поближе🐠")
    elif temp_today >= 20:
        text.append(f"Я счаслива, сейчас моя самая любимая температура - {temp_today:.1f}")
    return random.choice(text)


def tomorrow_weather(): # уже изменено
    temp_yesterday = weather.get_weather_average(1)
    text = f"Завтра на улице в среднем {temp_yesterday} градусов"
    temps = weather.get_weather(1)
    res = text + "\n\nТемпература на завтра:\nУтром: {}\nДнем: {}\nВечером: {}\nНочью: {}".format(*temps)
    return res


def today_weather(): # уже изменено
    temp_yesterday = weather.get_weather_average(0)
    text = f"Сегодня на улице в среднем {temp_yesterday} градусов"
    temps = weather.get_weather(0)
    res = text + "\n\nТемпература на сегодня:\nУтром: {}\nДнем: {}\nВечером: {}\nНочью: {}".format(*temps)
    return res


def joke():
    text = ["О, а я знаю один анекдот!", "Значит слушай..."]
    res = random.choice(text) + "\n" + anektod.get_joke()
    return res
