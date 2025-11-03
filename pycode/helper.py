# Импорт QT классов
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QIcon


###################################################################################################
# Функции для работы с окнами
###################################################################################################
def center_window(window):
    """Универсальная функция для центрирования любого окна на экране"""
    # Получаем геометрию экрана
    screen = QApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    
    # Получаем размер окна (учитывая frame)
    frame_geometry = window.frameGeometry()
    window_width = frame_geometry.width()
    window_height = frame_geometry.height()
    
    # Вычисляем позицию для центрирования
    x = (screen_geometry.width() - window_width) // 2
    y = (screen_geometry.height() - window_height) // 2
    
    # Устанавливаем позицию
    window.move(x, y)

\
def center_window_on_screen(window, screen_number=0):
    """Центрирование окна на конкретном экране (для многомониторных систем)"""
    screens = QApplication.screens()
    if screen_number < len(screens):
        screen = screens[screen_number]
    else:
        screen = QApplication.primaryScreen()
    
    screen_geometry = screen.availableGeometry()
    frame_geometry = window.frameGeometry()
    
    x = screen_geometry.left() + (screen_geometry.width() - frame_geometry.width()) // 2
    y = screen_geometry.top() + (screen_geometry.height() - frame_geometry.height()) // 2
    
    window.move(x, y)


def center_window_relative_to_parent(child_window, parent_window):
    """Центрирование дочернего окна относительно родительского"""
    parent_geometry = parent_window.frameGeometry()
    child_geometry = child_window.frameGeometry()
    
    x = parent_geometry.left() + (parent_geometry.width() - child_geometry.width()) // 2
    y = parent_geometry.top() + (parent_geometry.height() - child_geometry.height()) // 2
    
    child_window.move(x, y)


###################################################################################################
# Прочие функции
###################################################################################################
def show_message(text, info_text="", title="Система",
                 buttons=['Ok'],
                 icon='Information'):
    """
    Улучшенная версия функции для отображения сообщений с настройками

    Параметры:
        text (str): Основной текст сообщения
        info_text (str): Дополнительный информационный текст
        title (str): Заголовок окна
        buttons (list): Список кнопок ['Ok', 'Cancel', 'Yes', 'No', ...]
        icon (str): Тип иконки ('Information', 'Warning', 'Critical', 'Question', 'NoIcon')

    Возвращает:
        QMessageBox: настроенный диалог
    """
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)

    # Установка типа сообщения и иконки
    icon_mapping = {
        'Information': QMessageBox.Icon.Information,
        'Warning': QMessageBox.Icon.Warning,
        'Critical': QMessageBox.Icon.Critical,
        'Question': QMessageBox.Icon.Question,
        'NoIcon': QMessageBox.Icon.NoIcon
    }
    
    msg.setIcon(icon_mapping.get(icon, QMessageBox.Icon.Information))
    msg.setWindowIcon(QIcon(msg.iconPixmap()))

    # Установка дополнительного текста
    if info_text:
        msg.setInformativeText(info_text)

    # Маппинг кнопок из строк в StandardButton
    button_mapping = {
        'Ok': QMessageBox.StandardButton.Ok,
        'Open': QMessageBox.StandardButton.Open,
        'Save': QMessageBox.StandardButton.Save,
        'Cancel': QMessageBox.StandardButton.Cancel,
        'Close': QMessageBox.StandardButton.Close,
        'Yes': QMessageBox.StandardButton.Yes,
        'No': QMessageBox.StandardButton.No,
        'Abort': QMessageBox.StandardButton.Abort,
        'Retry': QMessageBox.StandardButton.Retry,
        'Ignore': QMessageBox.StandardButton.Ignore
    }

    # Русские названия кнопок
    button_texts = {
        'Ok': "ОК",
        'Open': "Открыть",
        'Save': "Сохранить",
        'Cancel': "Отмена",
        'Close': "Закрыть",
        'Yes': "Да",
        'No': "Нет",
        'Abort': "Прервать",
        'Retry': "Повторить",
        'Ignore': "Игнорировать"
    }

    # Собираем стандартные кнопки
    standard_buttons = QMessageBox.StandardButton.NoButton
    for btn in buttons:
        if btn in button_mapping:
            standard_buttons |= button_mapping[btn]

    msg.setStandardButtons(standard_buttons)

    # Устанавливаем русские названия кнопок
    for btn in buttons:
        if btn in button_mapping and btn in button_texts:
            button = msg.button(button_mapping[btn])
            if button:  # Проверка на случай, если кнопка не была создана
                button.setText(button_texts[btn])

    return msg
