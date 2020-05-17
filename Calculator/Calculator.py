import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy, QMessageBox
from PyQt5.QtGui import QIcon

class Calculadora(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Vitu')
        self.setFixedSize(300,350)
        self.setWindowIcon(QIcon('Icon2.png'))
        self.grid = QGridLayout()

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet('* {background: #FFF; color: #000; font-size: 30px;}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('8'), 1, 1, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('9'), 1, 2, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('+'), 1, 3, 1, 1, style='background: #129439; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(''), 'background: #D78113; color: #FFF; font-weight: 700')

        self.add_btn(QPushButton('4'), 2, 0, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('5'), 2, 1, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('6'), 2, 2, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('-'), 2, 3, 1, 1, style='background: #123594; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('<-'), 2, 4, 1, 1, lambda: self.display.setText(self.display.text()[:-1]), 'background: #EB0E22; color: #FFF; font-weight: 700')

        self.add_btn(QPushButton('1'), 3, 0, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('2'), 3, 1, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('3'), 3, 2, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('/'), 3, 3, 1, 1, style='background: #E6E01B; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton(''), 3, 4, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')

        self.add_btn(QPushButton('.'), 4, 0, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('0'), 4, 1, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton(''), 4, 2, 1, 1, style='background: #1999D1; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('*'), 4, 3, 1, 1, style='background: #E61BB5; color: #FFF; font-weight: 700')
        self.add_btn(QPushButton('='), 4, 4, 1, 1, self.eval_igual, 'background: #0EEB29; color: #FFF; font-weight: 700;')

        self.setLayout(self.grid)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(lambda: self.display.setText(self.display.text() + btn.text()))
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            msgbox = QMessageBox.critical(self, 'ERROR', f'ERRO: {e}')

if __name__ == '__main__':
    qt = QApplication([])
    calc = Calculadora()
    calc.show()
    sys.exit(qt.exec_())