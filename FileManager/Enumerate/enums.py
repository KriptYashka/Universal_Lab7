import enum


class Mode(enum.Enum):
    class Write(enum.Enum):
        type = "w"
        name = "Чтение файла"

    class Read(enum.Enum):
        type = "r"
        name = "Запись файла"


class Command(enum.IntEnum):
    exit = 0
    sort_up = 1
    sort_down = 2
    sort_rand = 3
    sort_len_up = 4
    sort_len_down = 5
