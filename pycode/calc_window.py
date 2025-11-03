from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class CalcWindow(QWidget):
    def __init__(self):
        super().__init__()
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