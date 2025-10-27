from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6 import QtCore, QtGui, uic
from PyQt6.uic import loadUi
import sys

class WikiWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/wiki_window.ui', self)
        
        self.dotaCheckBox.stateChanged.connect(self.on_dota_changed)
        self.csCheckBox.stateChanged.connect(self.on_cs_changed)
    
    def on_dota_changed(self, state):
        if state == 2:  # Checked
            print('Dota_CheckBox - Checked')
    
    def on_cs_changed(self, state):
        if state == 2:
            print('Cs_CheckBox - Checked')