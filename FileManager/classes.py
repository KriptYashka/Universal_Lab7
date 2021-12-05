from Enumerate.enums import Mode
import os


class File:
    def __init__(self, path, mode):
        self.path = path
        self.is_correct = 400
        self.mode = mode
        self.set_correct_file()

        if self.is_correct == 200:
            self.f = open(self.path, self.mode.value.type.value)

    def __del__(self):
        if self.is_correct == 200:
            self.f.close()

    def set_correct_file(self):
        if not os.path.exists(self.path):
            self.is_correct = 404
            return
        if not os.path.isfile(self.path):
            self.is_correct = 405
            return
        self.is_correct = 200
