from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

class WikiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Game Helper')
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        title = QLabel("Википедия")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
            }
        """)
        
        content = QLabel("Здесь будет содержимое википедии...")
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(title)
        layout.addWidget(content)
        self.setLayout(layout)