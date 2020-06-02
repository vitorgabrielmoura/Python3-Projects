import clipboard
from random import randint
import re
from design_app import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
import sys

class Validador(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(164, 217)
        self.setWindowTitle('Gerador/Validador CPF')
        self.setWindowIcon(QIcon('Icon2.png'))

        self.btnValidarCpf.clicked.connect(self.leitor_cpf)
        self.btnGerarCpf.clicked.connect(self.gerador_cpf)

    def leitor_cpf(self):
        texto = self.inputCPF.text()
        cpf = str(texto)
        cpf = re.sub(r'[^0-9]', '', cpf)

        if not cpf or len(cpf) != 11:
            self.message_box = QMessageBox.critical(self, 'ERRO', 'CPF Inválido!')
            return False

        novo_cpf = cpf[:-2]
        reverso = 10
        total = 0

        for i in range(19):
            total += int(novo_cpf[i-9]) * reverso
            reverso -= 1
            if i == 8 or i == 18:
                reverso = 11
                d = 11 - (total %11)
                if d > 9:
                    d = 0
                total = 0
                novo_cpf += str(d)

        sequencia = str(novo_cpf[0]) * len(cpf)

        if novo_cpf == cpf and cpf != sequencia:
            self.message_box = QMessageBox.information(self, 'Validação', 'CPF Válido!')
        else:
            self.message_box = QMessageBox.critical(self, 'Validação', 'CPF Inválido!')


    def gerador_cpf(self):
        numeros = randint(100000000, 999999999)

        novo_cpf = str(numeros)
        reverso = 10
        total = 0

        for i in range(19):
            total += int(novo_cpf[i-9]) * reverso
            reverso -= 1
            if i == 8 or i == 18:
                reverso = 11
                d = 11 - (total % 11)
                if d > 9:
                    d = 0
                total = 0
                novo_cpf += str(d)
        novo_cpf_formatado = f'{novo_cpf[0:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:11]}'

        if self.selectPontuacao.isChecked():
            self.lineCPFgerador.setText(novo_cpf_formatado)
        else:
            self.lineCPFgerador.setText(novo_cpf)

        if self.selectCopiar.isChecked():
            clipboard.copy(self.lineCPFgerador.text())

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    validador = Validador()
    validador.show()
    sys.exit(qt.exec_())
