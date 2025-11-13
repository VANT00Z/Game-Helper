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

    def add_html_about(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            self.aboutBrowser.setHtml(html_content)

    def back(self):
        """ Возврат в предыдущее окно """
        self.close()
