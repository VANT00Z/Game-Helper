import pycode.helper as hp

from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi


class CalcWindow(QWidget):
    def __init__(self, last_window):
        super().__init__()

        self.last_window = last_window

        loadUi('templates/calc.ui', self)

        self.setWindowIcon(QIcon('resources/icon.png'))
        self.setWindowTitle('Калькулятор')

        """ Моды """
        
        self.classicCheck.stateChanged.connect(self.classic_mode)
        self.classicCheck.setChecked(True)
        self.csCheck.stateChanged.connect(self.cs_mode)
        self.dotaCheck.stateChanged.connect(self.dota_mode)
        
        """ Кнопки classic mode"""
        
        self.plusButton.clicked.connect(self.calc_plus)
        self.minusButton.clicked.connect(self.calc_minus)
        self.divideButton.clicked.connect(self.calc_divide)
        self.multiplyButton.clicked.connect(self.calc_multiply)
        self.oneButton.clicked.connect(self.calc_one)
        self.twoButton.clicked.connect(self.calc_two)
        self.threeButton.clicked.connect(self.calc_three)
        self.fourButton.clicked.connect(self.calc_four)
        self.fiveButton.clicked.connect(self.calc_five)
        self.sixButton.clicked.connect(self.calc_six)
        self.sevenButton.clicked.connect(self.calc_seven)
        self.eightButton.clicked.connect(self.calc_eight)
        self.nineButton.clicked.connect(self.calc_nine)
        self.zeroButton.clicked.connect(self.calc_zero)
        self.equalsButton.clicked.connect(self.calc_equals)
        self.resetButton.clicked.connect(self.calc_reset)

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

    """ Функции classic mode"""

    def calc_plus(self):
        self.answer.setText(self.answer.text() + '+')

    def calc_minus(self):
        self.answer.setText(self.answer.text() + '-')

    def calc_multiply(self):
        self.answer.setText(self.answer.text() + '*')

    def calc_divide(self):
        self.answer.setText(self.answer.text() + '/')

    def calc_one(self):
        self.answer.setText(self.answer.text() + '1')

    def calc_two(self):
        self.answer.setText(self.answer.text() + '2')

    def calc_three(self):
        self.answer.setText(self.answer.text() + '3')

    def calc_four(self):
        self.answer.setText(self.answer.text() + '4')

    def calc_five(self):
        self.answer.setText(self.answer.text() + '5')

    def calc_six(self):
        self.answer.setText(self.answer.text() + '6')

    def calc_seven(self):
        self.answer.setText(self.answer.text() + '7')

    def calc_eight(self):
        self.answer.setText(self.answer.text() + '8')

    def calc_nine(self):
        self.answer.setText(self.answer.text() + '9')

    def calc_zero(self):
        self.answer.setText(self.answer.text() + '0')

    def calc_equals(self):
        self.answer.setText(
            f'{self.answer.text()} = {eval(self.answer.text())}')

    def calc_reset(self):
        self.answer.setText('')

    def back(self):
        """ Возврат в предыдущее окно """
        self.last_window.show()
        hp.center_window(self.last_window)
        self.close()

    def classic_mode(self, state):
        if state == 0:
            print('classic off')
        elif state == 2:
            print('classic on')

    def cs_mode(self, state):
        if state == 0:
            print('cs off')
        elif state == 2:
            print('cs on')

    def dota_mode(self, state):
        if state == 0:
            print('dota off')
        elif state == 2:
            print('dota on')