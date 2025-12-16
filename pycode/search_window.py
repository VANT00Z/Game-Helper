import pycode.helper as hp
import re
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi


class SearchWindow(QWidget):
    def __init__(self, last_window):
        super().__init__()

        self.last_window = last_window

        loadUi('templates/search.ui', self)

        self.setWindowIcon(QIcon('resources/Logo 3.png'))
        self.setWindowTitle('Поиск')

        self.searchLine.setPlaceholderText("Введите запрос для поиска...")

        self.resultLabel.hide()

        self.searchLine.returnPressed.connect(
            lambda: self.perform_search(self.searchLine.text()))

        self.searchButton.clicked.connect(
            lambda: self.perform_search(self.searchLine.text()))

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

    def perform_search(self, request=None):
        """Выполняет поиск и показывает результаты"""
        if not request or request.strip() == "":
            self.searchBrowser.setHtml("<p>Введите поисковый запрос</p>")
            return

        request = request.strip()
        self.resultLabel.setText(f'Результаты поиска по запросу: {request}')
        self.resultLabel.show()

        # Читаем содержимое HTML файлов
        dota_content = ""
        cs_content = ""
        
        try:
            with open('texts/dota_wiki/dota_wiki.html', 'r', encoding='utf-8') as file:
                dota_content = file.read()
        except FileNotFoundError:
            dota_content = "<p>Файл Dota 2 wiki не найден</p>"
        
        try:
            with open('texts/cs_wiki/cs_wiki.html', 'r', encoding='utf-8') as file:
                cs_content = file.read()
        except FileNotFoundError:
            cs_content = "<p>Файл CS wiki не найден</p>"

        # Формируем HTML с результатами поиска
        result_html = self.generate_search_results(request, dota_content, cs_content)
        self.searchBrowser.setHtml(result_html)

    def extract_text_from_html(self, html_content):
        """Извлекает только текстовый контент из HTML, игнорируя CSS и скрипты"""
        # Удаляем содержимое тегов style и script
        content_without_style_script = re.sub(
            r'<(style|script)[^>]*>.*?</\1>', 
            ' ', 
            html_content, 
            flags=re.DOTALL
        )
        
        # Удаляем все HTML теги, оставляя только текст
        text_only = re.sub(r'<[^>]+>', ' ', content_without_style_script)
        
        # Заменяем множественные пробелы на один
        text_only = re.sub(r'\s+', ' ', text_only)
        
        return text_only.strip()

    def generate_search_results(self, request, dota_content, cs_content):
        """Генерирует HTML с результатами поиска"""
        words = request.lower().split()
        
        # Функция для поиска и выделения совпадений
        def search_in_content(content, title):
            # Извлекаем только текстовый контент, игнорируя CSS
            text_only = self.extract_text_from_html(content)
            
            results = []
            lines = text_only.split('. ')  # Разбиваем на предложения
            
            for line in lines:
                if not line.strip():
                    continue
                    
                line_lower = line.lower()
                # Проверяем, содержит ли строка все слова запроса
                if all(word in line_lower for word in words):
                    # Выделяем найденные слова в тексте
                    highlighted_line = line
                    for word in words:
                        pattern = re.compile(re.escape(word), re.IGNORECASE)
                        highlighted_line = pattern.sub(
                            f'<span style="background-color: yellow; font-weight: bold;">{word.upper()}</span>', 
                            highlighted_line
                        )
                    results.append(highlighted_line)
                    
                    # Ограничиваем количество результатов
                    if len(results) >= 5:
                        break
            
            return results, title

        # Поиск в обоих источниках
        dota_results, dota_title = search_in_content(dota_content, "Dota 2 Wiki")
        cs_results, cs_title = search_in_content(cs_content, "CS:GO 2 Wiki")

        # Формируем итоговый HTML
        html_result = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ 
                    font-family: Arial, sans-serif; 
                    margin: 20px; 
                    line-height: 1.6;
                }}
                .section {{ 
                    margin-bottom: 30px; 
                    padding: 15px;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                }}
                .title {{ 
                    font-size: 20px; 
                    font-weight: bold; 
                    color: #2c3e50; 
                    margin-bottom: 15px;
                    padding-bottom: 10px;
                    border-bottom: 2px solid #3498db;
                }}
                .result {{ 
                    margin-bottom: 12px; 
                    padding: 8px;
                    background-color: #f8f9fa;
                    border-left: 4px solid #3498db;
                }}
                .no-results {{ 
                    color: #7f8c8d; 
                    font-style: italic;
                    padding: 10px;
                }}
                mark {{
                    background-color: yellow;
                    font-weight: bold;
                    padding: 2px;
                }}
                .source-info {{
                    font-size: 14px;
                    color: #27ae60;
                    margin-bottom: 5px;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            
        """

        # Добавляем результаты Dota 2
        html_result += f'<div class="section"><div class="title">{dota_title}</div>'
        if dota_results:
            for result in dota_results:
                html_result += f'<div class="result">{result}</div>'
        else:
            html_result += '<div class="result no-results">Совпадений не найдено</div>'
        html_result += '</div>'

        # Добавляем результаты CS:GO
        html_result += f'<div class="section"><div class="title">{cs_title}</div>'
        if cs_results:
            for result in cs_results:
                html_result += f'<div class="result">{result}</div>'
        else:
            html_result += '<div class="result no-results">Совпадений не найдено</div>'
        html_result += '</div>'

        html_result += "</body></html>"
        return html_result

    def back(self):
        """ Возврат в предыдущее окно """
        self.last_window.show()
        hp.center_window(self.last_window)
        self.close()