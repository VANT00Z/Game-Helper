import pycode.helper as hp

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class CalcWindow(QWidget):
    def __init__(self, last_window):
        super().__init__()
        
        self.last_window = last_window
        
        self.setWindowIcon(QIcon('resources/icon.png'))
        self.setWindowTitle('Калькулятор')
        
        self.init_ui()
    
    def init_ui(self):
        # Создаем вертикальный layout
        layout = QVBoxLayout()
        
        # Создаем заголовок "Калькулятор"
        title = QLabel("Калькулятор")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
            }
        """)
        
        # Добавляем заголовок в layout
        layout.addWidget(title)
        
        # Устанавливаем layout для виджета
        self.setLayout(layout)
        
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
        
    def back(self):
        """ Возврат в предыдущее окно """
        self.last_window.show()
        hp.center_window(self.last_window)
        self.close()