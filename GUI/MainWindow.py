import json

from PySide2.QtWidgets import QMainWindow


def load_config():
    return json.load(open('config.json', 'r'))


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.config = load_config()

        self.setWindowTitle("Storage Manager")

        self.set_size()

    def set_size(self):
        self.width = self.config["resolution"]["width"]
        self.height = self.config["resolution"]["height"]
        self.resize(self.width, self.height)
