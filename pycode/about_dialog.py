from PyQt6.QtWidgets import QDialog, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()

        loadUi('templates/about.ui', self)

        self.setWindowIcon(QIcon('resources/icon.png'))
        self.setWindowTitle('About')

        self.add_html_about("texts/about/about.html")

    def add_html_about(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            self.aboutBrowser.setHtml(html_content)
