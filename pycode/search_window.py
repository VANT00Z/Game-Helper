import pycode.helper as hp

from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi


class SearchWindow(QWidget):
    def __init__(self, last_window):
        super().__init__()

        self.last_window = last_window

        loadUi('templates/search.ui', self)

        self.setWindowIcon(QIcon('resources/icon.png'))
        self.setWindowTitle('Поиск')

        self.searchLine.setPlaceholderText("Введите запрос для поиска...")

        self.resultLabel.hide()

        self.searchLine.returnPressed.connect(
            lambda: self.perform_search(self.searchLine.text()))

        self.searchButton.clicked.connect(
            lambda: self.perform_search(self.searchLine.text()))

        self.back_btn = QPushButton('<-', self)
        self.back_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(217, 217, 217, 1);
                color: #333;
                text-decoration: none;
                border-radius: 10px;
                font-weight: 900;
                font-size: 24px;
            }
        """)
        self.back_btn.resize(40, 20)
        self.back_btn.clicked.connect(self.back)

    def perform_search(self, request=None):
        """Выполняет поиск и показывает результаты"""
        if request:
            self.resultLabel.setText(
                f'Результаты поиска по запросу: {request}')
            self.resultLabel.show()
            word_request = request.split()

            # читаем html Dota 2
            with open('texts\dota_wiki\dota_wiki.html', 'r', encoding='utf-8') as file:
                dota_cont = file.read()

            # читаем html Cs2
            with open('texts\cs_wiki\cs_wiki.html', 'r', encoding='utf-8') as file:
                cs_cont = file.read()

            for word in word_request:
                if len(word_request) > 1:

                    if word in dota_cont:
                        ind_dota = dota_cont.index(word)
                        self.searchBrowser.setHtml(dota_cont[ind_dota])
                    else:
                        print('Не найдено')

                else:
                    if request in dota_cont:
                        self.searchBrowser.setHtml(request)
                    else:
                        print('Не найдено')

    def back(self):
        """ Возврат в предыдущее окно """
        self.last_window.show()
        hp.center_window(self.last_window)
        self.close()
