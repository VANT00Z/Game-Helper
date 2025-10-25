import os
import sys

from pycode.main_window import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore, QtWidgets


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
    

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

if __name__ == '__main__':
    os.system("cls")
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())