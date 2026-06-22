import pycode.helper as hp

from PyQt6.QtWidgets import QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi


class SteamWindow(QWidget):
    def __init__(self, last_window):
        super().__init__()

        self.last_window = last_window

        loadUi('templates/steamsearch.ui', self)

        self.setWindowIcon(QIcon('resources/Logo 3.png'))
        self.setWindowTitle('SteamSearch')
        
        menu = QMenu()
        menu.addAction(self.actionSteamId)
        menu.addAction(self.actionAppId)
        menu.addAction(self.actionNews)
        self.otherFunctionsBtn.setMenu(menu)
