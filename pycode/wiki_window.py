import pycode.helper as hp

from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi


class WikiWindow(QWidget):
    def __init__(self, last_window):
        super().__init__()

        self.last_window = last_window

        loadUi('templates/wiki_window.ui', self)

        self.setWindowIcon(QIcon('resources/icon.png'))
        self.setWindowTitle('wiki')

        self.dotaCheckBox.stateChanged.connect(self.on_dota_changed)
        self.csCheckBox.stateChanged.connect(self.on_cs_changed)

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

        self.add_html_dota('texts\dota_wiki\dota_wiki.html')
        self.add_html_cs('texts\cs_wiki\cs_wiki.html')

    def add_html_dota(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            self.textDota.setHtml(html_content)

    def add_html_cs(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            self.textCs.setHtml(html_content)

    '''Ивент добавления фильтров'''

    def on_dota_changed(self, state):
        if state == 2:
            self.textCs.hide()
        elif state == 0:
            self.textCs.show()

    def on_cs_changed(self, state):
        if state == 2:
            self.textDota.hide()
        elif state == 0:
            self.textDota.show()

    def back(self):
        """ Возврат в предыдущее окно """
        self.last_window.show()
        hp.center_window(self.last_window)
        self.close()
