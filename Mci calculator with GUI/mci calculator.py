import sys
from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel, QApplication
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('IMC')
        self.setWindowIcon(QIcon('Icon2.ico'))

        self.botao = QPushButton('Enviar')

        self.linha1 = QLineEdit()
        self.linha1.setPlaceholderText('Ex: 50.2 Kg')
        self.linha2 = QLineEdit()
        self.linha2.setPlaceholderText('Ex: 1.65 m')
        self.botao.clicked.connect(self.exibir)

        self.layout = QGridLayout()
        self.label = QLabel('Peso:')
        self.label2 = QLabel('Altura:')
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.linha1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.linha2)
        self.layout.addWidget(self.botao)
        self.setLayout(self.layout)

    def exibir(self):
        try:
            peso = self.linha1.text()
            altura = self.linha2.text()
            alturaa = float(altura)
            self.imc = float(peso) / (alturaa**2)
            sits = ['Abaixo do peso', 'com Peso Ideal', 'Levemente acima do peso', 'com Obesidade leve', 'com Obesidade severa', 'com Obesidade mórbida']
            imcs = [18.5, 24.9, 29.9, 34.9, 39.9]
            for s, i in zip(sits, imcs):
                if self.imc < i:
                    sitt = s
                    break
            self.messagebox = QMessageBox.information(self, 'Informativo', f'Seu índice de massa corporal é {self.imc:.2f}\nVocê está {sitt}')
        except ValueError:
            self.messagebox = QMessageBox.critical(self, 'Informativo', f'Erro: Digite um valor válido\nUse "." ao invés da vírgula')
        except Exception as e:
            self.messagebox = QMessageBox.critical(self, 'Informativo', f'Erro desconhecido: {e}')



if __name__ == '__main__':
    appctxt = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(appctxt.exec_())