from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        main_layout = QVBoxLayout()
        
        # Создаем поисковую строку
        search_layout = QHBoxLayout()
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Введите запрос для поиска...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 14px;
                border: 2px solid #ccc;
                border-radius: 5px;
            }
        """)
        
        search_button = QPushButton("Найти")
        search_button.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                font-size: 14px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        
        # Заголовок
        title = QLabel("Поиск")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
            }
        """)
        
        # Область для результатов
        self.results_label = QLabel("Результаты поиска будут отображаться здесь...")
        self.results_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.results_label.setStyleSheet("""
            QLabel {
                padding: 20px;
                color: #666;
            }
        """)
        
        # Добавляем все в основной layout
        main_layout.addWidget(title)
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.results_label)
        
        self.setLayout(main_layout)
        
        # Подключаем кнопку поиска
        search_button.clicked.connect(self.perform_search)
        self.search_input.returnPressed.connect(self.perform_search)
    
    def perform_search(self):
        """Выполняет поиск и показывает результаты"""
        query = self.search_input.text().strip()
        if query:
            self.results_label.setText(f"Поиск: {query}\n\nРезультаты будут отображаться здесь...")