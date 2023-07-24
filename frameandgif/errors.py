class GIFBadFormat(Exception):
    def __init__(self):
        self.message = "Неверный формат вывода для GIF"

    def __str__(self):
        return self.message