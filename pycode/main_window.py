import sys
import pycode.helper as hp

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi

""" Импортируем другие окна """
from pycode.wiki_window import WikiWindow
from pycode.calc_window import CalcWindow
from pycode.search_window import SearchWindow
from pycode.about_dialog import AboutDialog

""" Стартуем """


class MainWindow(QMainWindow):
    def __init__(self, last_window=None):
        """ Фундамент """
        super().__init__()
        loadUi('templates/main_window.ui', self)

        """ Задаем иконку и название """
        self.setWindowIcon(QIcon('resources/Logo 3.png'))
        self.setWindowTitle('Game Helper')

        self.last_window = last_window  # <- Инициируем последнее окно

        """ Кнопки """
        self.wiki_btn.clicked.connect(self.show_wiki)
        self.calc_btn.clicked.connect(self.show_calc)
        self.search_btn.clicked.connect(self.show_search)

        ''' Кнопки плашки'''
        self.actionAbout.triggered.connect(self.show_about)
        self.actionW.triggered.connect(self.show_wiki)
        self.actionCalc.triggered.connect(self.show_calc)
        self.actionSearch.triggered.connect(self.show_search)

    def back(self):
        """ Возврат в предыдущее окно """
        self.last_window.show()
        hp.center_window(self.last_window)
        self.last_window.default()
        self.close()

    def show_wiki(self):
        """Переключение на окно Вики"""
        self.wiki_window = WikiWindow(self)
        self.wiki_window.show()
        hp.center_window(self.wiki_window)
        self.hide()

    def show_calc(self):
        """Переключение на окно Калькулятора"""
        self.calc_window = CalcWindow(self)
        self.calc_window.show()
        hp.center_window(self.calc_window)
        self.hide()

    def show_search(self):
        """Переключение на окно Поиска"""
        self.search_window = SearchWindow(self)
        self.search_window.show()
        hp.center_window(self.search_window)
        self.hide()

    def show_about(self):
        """Переключение на окно Поиска"""
        self.about_window = AboutDialog()
        hp.center_window(self.about_window)
        self.about_window.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
