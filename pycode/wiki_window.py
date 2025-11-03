import pycode.helper as hp

from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi

class WikiWindow(QWidget):
    def __init__(self, last_window):
        
        self.last_window = last_window
        super().__init__()
        loadUi('templates/wiki_window.ui', self)
        
        self.setWindowIcon(QIcon('resources/icon.png'))
        self.setWindowTitle('wiki')

        self.dotaCheckBox.stateChanged.connect(self.on_dota_changed)
        self.csCheckBox.stateChanged.connect(self.on_cs_changed)

        self.back_btn = QPushButton('<-', self)
        self.back_btn.resize(100, 100)
        self.back_btn.clicked.connect(self.back)
    
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