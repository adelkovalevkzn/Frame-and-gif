import argparse


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="python3 main.py",
            description="Извечение кадра и создание GIF",
            epilog="-m (Методы): extract_frame (-a [timestamp]), create_gif (-a [начало] [длительность])"
        )

        self.parser.add_argument('filename')
        self.parser.add_argument('-m', '--method')
        self.parser.add_argument('-p', '--params', nargs='*')
        self.parser.add_argument('-o', '--output')

    def get_parser(self):
        return self.parser
