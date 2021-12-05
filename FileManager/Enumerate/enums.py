import enum


class Mode(enum.Enum):
    class Write(enum.Enum):
        type = "w"
        name = "Чтение файла"

    class Read(enum.Enum):
        type = "r"
        name = "Запись файла"
