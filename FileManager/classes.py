import os
from random import shuffle

from Enumerate.enums import Mode


class File:
    """Класс текстового файла. Включена обработка ошибок."""
    def __init__(self, path: str, mode):
        self.path = path
        self.is_correct = 400
        self.mode = mode
        self.data = []
        self.f = None

        self.set_correct()

        if self.is_correct == 200 and self.mode == Mode.Read:
            self.f = open(self.path, self.mode.value.type.value)
            self.data = self.f.readlines()

    def __del__(self):
        if self.is_correct == 200:
            self.f.close()

    def set_correct(self):
        """Проверка файла на корректность"""
        self.is_correct = 200
        if self.mode == Mode.Read:
            if not os.path.exists(self.path):
                self.is_correct = 404
            elif not os.path.isfile(self.path):
                self.is_correct = 405

    def write_file(self, data: list):
        if self.mode != Mode.Write and self.is_correct == 200:
            return 403
        self.f = open(self.path, self.mode.value.type.value)
        self.data = data
        self.f.writelines(data)
        self.f.close()

    def sort_up(self):
        """Сортировка строк файла по возрастанию"""
        if self.mode == Mode.Read:
            self.data.sort()

    def sort_down(self):
        """Сортировка строк файла по убыванию"""
        if self.mode == Mode.Read:
            self.data.sort(reverse=True)

    def sort_random(self):
        """Случайное перемешивание строк в файле"""
        if self.mode == Mode.Read:
            shuffle(self.data)

    def sort_length_up(self):
        """Сортировка строк файла по возрастанию их длины"""
        if self.mode == Mode.Read:
            self.data.sort(key=len)

    def sort_length_down(self):
        """Сортировка строк файла по убыванию их длины"""
        if self.mode == Mode.Read:
            self.data.sort(key=len, reverse=True)