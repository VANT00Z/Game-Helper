import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi

from pycode.calc_window import CalcWindow
from .wiki_window import WikiWindow
from .search_window import SearchWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Game Helper')
        
        # Создаем stacked widget для управления страницами
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Создаем экземпляры окон
        self.main_page = self.create_main_page()
        self.calc_window = CalcWindow()
        self.wiki_window = WikiWindow()
        self.search_window = SearchWindow()
        
        # Добавляем окна в stacked widget
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.calc_window)
        self.stacked_widget.addWidget(self.wiki_window)
        self.stacked_widget.addWidget(self.search_window)
        
        # Подключаем кнопки
        self.main_page.pushButton_2.clicked.connect(self.show_calculator)
        self.main_page.pushButton.clicked.connect(self.show_wiki)
        self.main_page.pushButton_3.clicked.connect(self.show_search)
        
    
    def create_main_page(self):
        """Создает главную страницу из UI файла"""
        widget = QMainWindow()  # Изменено с QMainWindow на QWidget
        loadUi('templates/main_window.ui', widget)
        return widget
    
    def show_calculator(self):
        """Переключает на окно калькулятора"""
        self.stacked_widget.setCurrentWidget(self.calc_window)
        self.setWindowTitle('Calc')
    
    def show_wiki(self):
        """Переключает на окно википедии"""
        self.stacked_widget.setCurrentWidget(self.wiki_window)
        self.setWindowTitle('Wiki')
    
    def show_search(self):
        """Переключает на окно поиска"""
        self.stacked_widget.setCurrentWidget(self.search_window)
        self.setWindowTitle('Search')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())