from classes import File
from Enumerate.enums import Mode


def is_correct_input(cmd):
    if cmd.isdigit():
        cmd = int(cmd)
        if cmd >= 0:
            return True
    return False


def choose_option():
    text = "1. сортировка всех строк по возрастанию\n2. сортировка всех строк по убыванию\n3. рандомное перемешивание "
    text += "всех строк\n4. сортировка всех строк по возрастанию их длины\n5. сортировка всех строк по убыванию их"
    text += "длины\n0. Выход\n--------\nВыбор: "
    cmd = input()
    if not is_correct_input(cmd):
        return 0


def main():
    text = "Добро пожаловать в программу KriptYashka!\n"
    print(text)
    test = File("input.txt", Mode.Read)
    while True:
        cod = choose_option()
        if cod:
            break
    text = "Программа завершила работу, до скорой встречи!"
    print(text)


if __name__ == '__main__':
    main()
