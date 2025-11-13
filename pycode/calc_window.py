import pycode.helper as hp

from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi


class CalcWindow(QWidget):
    def __init__(self, last_window):
        super().__init__()

        self.last_window = last_window

        loadUi('templates/calc.ui', self)

        self.setWindowIcon(QIcon('resources/Logo 3.png'))
        self.setWindowTitle('Калькулятор')

        """ Функционал classic mode """
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

        """ Функционал dota mode """
        self.numsLine.setPlaceholderText("Введите количество очков")

        self.strengthCheck.clicked.connect(lambda: self.dota_check_s())
        self.dexterityCheck.clicked.connect(lambda: self.dota_check_d())
        self.intelligenceCheck.clicked.connect(lambda: self.dota_check_i())

        self.resultButton.clicked.connect(self.dota_result)

        """ Функционал cs mode """

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

        self.akCheck.clicked.connect(lambda: self.set_gun('ak'))
        self.m4a4Check.clicked.connect(lambda: self.set_gun('m4a4'))
        self.glockCheck.clicked.connect(lambda: self.set_gun('glock'))
        self.p2000Check.clicked.connect(lambda: self.set_gun('p2000'))
        self.uspCheck.clicked.connect(lambda: self.set_gun('usp'))

        self.headButton.clicked.connect(lambda: self.res_possition('head'))
        self.handsButton.clicked.connect(lambda: self.res_possition('hands'))
        self.torsoButton.clicked.connect(lambda: self.res_possition('torso'))
        self.legsButton.clicked.connect(lambda: self.res_possition('legs'))

    """ Функции classic mode """

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

    """ Функции dota mode """

    def dota_check_s(self):
        if self.strengthCheck.isChecked:
            self.attribute = 'strength'
            self.dexterityCheck.setChecked(False)
            self.intelligenceCheck.setChecked(False)
        else:
            self.attribute = ''

    def dota_check_d(self):
        if self.dexterityCheck.isChecked:
            self.attribute = 'dexterity'
            self.strengthCheck.setChecked(False)
            self.intelligenceCheck.setChecked(False)
        else:
            self.attribute = ''

    def dota_check_i(self):
        if self.intelligenceCheck.isChecked:
            self.attribute = 'intelligence'
            self.dexterityCheck.setChecked(False)
            self.strengthCheck.setChecked(False)
        else:
            self.attribute = ''

    def dota_result(self):
        if self.attribute == 'strength':
            self.resultLabel_2.setText(
                f'Герой атрибута Сила получит: \n {int(self.numsLine.text()) * 22} здоровья \n {int(self.numsLine.text()) + 0.1} Восстановление здоровья')

        elif self.attribute == 'dexterity':
            self.resultLabel_2.setText(
                f'Герой атрибута Ловкость получит: \n {int(self.numsLine.text()) * 0.167} брони \n {int(self.numsLine.text())} скорость атаки')

        elif self.attribute == 'intelligence':
            self.resultLabel_2.setText(
                f'Герой атрибута Интелект получит: \n Максимальный запас маны увеличится на {int(self.numsLine.text()) * 12} \n {int(self.numsLine.text()) * 0.05} восстановвление маны \n {int(self.numsLine.text()) * 0.001} сопротивление магии')

        else:
            self.resultLabel_2.setText('Выберите атрибут')

    """ Функции cs mode """

    def set_gun(self, gun):
        self.gun = gun

    cs_dict_head = {
        'ak': '108',
        'm4a4': '109',
        'glock': '71',
        'p2000': '73',
        'usp': '75',
    }

    cs_dict_hands = {
        'ak': '80',
        'm4a4': '82',
        'glock': '40',
        'p2000': '37',
        'usp': '56',
    }

    cs_dict_torso = {
        'ak': '40',
        'm4a4': '40',
        'glock': '11',
        'p2000': '14',
        'usp': '10',
    }

    cs_dict_legs = {
        'ak': '0',
        'm4a4': '0',
        'glock': '0',
        'p2000': '0',
        'usp': '0',
    }

    def res_possition(self, point):
        self.point = point

        if self.point == 'head':
            self.resultLabel.setText(
                f'оружие {self.gun} нанесет {self.cs_dict_head[self.gun]} урона')
        elif self.point == 'hands':
            self.resultLabel.setText(
                f'оружие {self.gun} нанесет {self.cs_dict_hands[self.gun]} урона')
        elif self.point == 'torso':
            self.resultLabel.setText(
                f'оружие {self.gun} нанесет {self.cs_dict_torso[self.gun]} урона')
        elif self.point == 'legs':
            self.resultLabel.setText(
                f'оружие {self.gun} нанесет {self.cs_dict_legs[self.gun]} урона')

    def back(self):
        """ Возврат в предыдущее окно """
        self.last_window.show()
        hp.center_window(self.last_window)
        self.close()
