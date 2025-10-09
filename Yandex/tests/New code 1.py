import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Коля чушпан')
        self.lbl = QLabel (self)
        self.lbl.move(90,40)
        self.lbl.setText('Пипидастр')
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())