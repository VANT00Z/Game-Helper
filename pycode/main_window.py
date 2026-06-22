import sys
import pycode.helper as hp

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi

from pycode.wiki_window import WikiWindow
from pycode.calc_window import CalcWindow
from pycode.search_window import SearchWindow
from pycode.about_dialog import AboutDialog
from pycode.steam_search import SteamWindow


class MainWindow(QMainWindow):
    def __init__(self, last_window=None):
        super().__init__()
        loadUi('templates/main_window.ui', self)

        self.setWindowIcon(QIcon('resources/Logo 3.png'))
        self.setWindowTitle('Game Helper')

        self.last_window = last_window

        self.wiki_btn.clicked.connect(self.show_wiki)
        self.calc_btn.clicked.connect(self.show_calc)
        self.search_btn.clicked.connect(self.show_search)

        self.actionAbout.triggered.connect(self.show_about)
        self.actionW.triggered.connect(self.show_wiki)
        self.actionCalc.triggered.connect(self.show_calc)
        self.actionSearch.triggered.connect(self.show_search)

    def back(self):
        self.last_window.show()
        hp.center_window(self.last_window)
        self.last_window.default()
        self.close()

    def show_wiki(self):
        self.wiki_window = WikiWindow(self)
        self.wiki_window.show()
        hp.center_window(self.wiki_window)
        self.hide()

    def show_calc(self):
        self.calc_window = CalcWindow(self)
        self.calc_window.show()
        hp.center_window(self.calc_window)
        self.hide()

    def show_search(self):
        self.search_window = SearchWindow(self)
        self.search_window.show()
        hp.center_window(self.search_window)
        self.hide()

    def show_steam(self):
        self.steam_window = SteamWindow()
        hp.center_window(self.steam_window)
        self.steam_window.show()
        self.hide()

    def show_about(self):
        self.about_window = AboutDialog()
        hp.center_window(self.about_window)
        self.about_window.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
