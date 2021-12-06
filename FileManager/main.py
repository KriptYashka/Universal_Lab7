from classes import File
from Enumerate.enums import Mode, Command


def is_correct_input(cmd):
    if cmd.isdigit():
        if int(cmd) >= 0:
            return True
    return False


def main():
    text = "Добро пожаловать в программу KriptYashka!\nВыберите входной файл: "
    print(text)
    # path = input()
    # fin = File(path, Mode.Read)
    fin = File("files/input.txt", Mode.Read)
    # text = "Выберите выходной файл: "
    # pathOut = input()
    # fout = File(pathOut, Mode.Write)
    fout = File("files/output.txt", Mode.Write)
    while True:
        text = "1. Сортировка всех строк по возрастанию\n2. Сортировка всех строк по убыванию\n3. Рандомное " \
               "перемешивание всех строк\n4. Сортировка всех строк по возрастанию их длины\n5. Сортировка всех строк " \
               "по убыванию их длины\n0. Выход\n--------\nВыбор: "
        print(text)
        cmd = input()
        if not is_correct_input(cmd):
            continue
        cmd = int(cmd)
        if cmd == Command.sort_up.value:
            fin.sort_up()
        elif cmd == Command.sort_down.value:
            fin.sort_down()
        elif cmd == Command.sort_rand.value:
            fin.sort_random()
        elif cmd == Command.sort_len_up.value:
            fin.sort_length_up()
        elif cmd == Command.sort_len_down.value:
            fin.sort_length_down()
        elif cmd == Command.exit.value:
            break
        fout.write_file(fin.data)
        print("Операция выполнена\n~~~~~~~~~~~~~~~~\n")

    text = "Программа завершила работу, до скорой встречи!"
    print(text)


if __name__ == '__main__':
    main()
