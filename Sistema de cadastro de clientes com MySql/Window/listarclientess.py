import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListarClientes(object):
    def setupUi(self, ListarClientes):
        _translate = QtCore.QCoreApplication.translate

        ListarClientes.setObjectName("ListarClientes")
        ListarClientes.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(ListarClientes)
        self.centralwidget.setObjectName("centralwidget")
        ListarClientes.setWindowTitle(_translate("ListarClientes", "ListarClientes"))


        self.cliente1 = QtWidgets.QLineEdit(self.centralwidget)
        self.cliente1.setGeometry(QtCore.QRect(10, 10, 251, 20))
        self.cliente1.setObjectName("cliente1")
        self.cliente1.setDisabled(True)

        self.h1 = QtWidgets.QPushButton(self.centralwidget)
        self.h1.setGeometry(QtCore.QRect(270, 10, 75, 23))
        self.h1.setObjectName("h1")
        self.h1.setText(_translate("ListarClientes", "Histórico"))

        self.n1 = QtWidgets.QPushButton(self.centralwidget)
        self.n1.setGeometry(QtCore.QRect(350, 10, 75, 23))
        self.n1.setObjectName("n1")
        self.n1.setText(_translate("ListarClientes", "Novo serviço"))

        self.e1 = QtWidgets.QPushButton(self.centralwidget)
        self.e1.setGeometry(QtCore.QRect(430, 10, 75, 23))
        self.e1.setObjectName("e1")
        self.e1.setText(_translate("ListarClientes", "Editar dados"))

        self.d1 = QtWidgets.QPushButton(self.centralwidget)
        self.d1.setGeometry(QtCore.QRect(510, 10, 75, 23))
        self.d1.setObjectName("d1")
        self.d1.setText(_translate("ListarClientes", "Deletar"))



        self.cliente2 = QtWidgets.QLineEdit(self.centralwidget)
        self.cliente2.setGeometry(QtCore.QRect(10, 40, 251, 20))
        self.cliente2.setObjectName("cliente2")
        self.cliente2.setDisabled(True)

        self.h2 = QtWidgets.QPushButton(self.centralwidget)
        self.h2.setGeometry(QtCore.QRect(270, 40, 75, 23))
        self.h2.setObjectName("h2")
        self.h2.setText(_translate("ListarClientes", "Histórico"))

        self.n2 = QtWidgets.QPushButton(self.centralwidget)
        self.n2.setGeometry(QtCore.QRect(350, 40, 75, 23))
        self.n2.setObjectName("n2")
        self.n2.setText(_translate("ListarClientes", "Novo serviço"))

        self.e2 = QtWidgets.QPushButton(self.centralwidget)
        self.e2.setGeometry(QtCore.QRect(430, 40, 75, 23))
        self.e2.setObjectName("e2")
        self.e2.setText(_translate("ListarClientes", "Editar dados"))

        self.d2 = QtWidgets.QPushButton(self.centralwidget)
        self.d2.setGeometry(QtCore.QRect(510, 40, 75, 23))
        self.d2.setText(_translate("ListarClientes", "Deletar "))


        ListarClientes.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(ListarClientes)

    def criar_modelo(self):
        for c in range(0,4):
            _translate = QtCore.QCoreApplication.translate

            self.cliente1 = QtWidgets.QLineEdit(self.centralwidget)
            self.cliente1.setGeometry(QtCore.QRect(10, 10, 251, 20))
            self.cliente1.setObjectName("cliente1")

            self.h1 = QtWidgets.QPushButton(self.centralwidget)
            self.h1.setGeometry(QtCore.QRect(270, 10, 75, 23))
            self.h1.setObjectName("h1")
            self.h1.setText(_translate("ListarClientes", "Histórico"))

            self.n1 = QtWidgets.QPushButton(self.centralwidget)
            self.n1.setGeometry(QtCore.QRect(350, 10, 75, 23))
            self.n1.setObjectName("n1")
            self.n1.setText(_translate("ListarClientes", "Novo serviço"))

            self.e1 = QtWidgets.QPushButton(self.centralwidget)
            self.e1.setGeometry(QtCore.QRect(430, 10, 75, 23))
            self.e1.setObjectName("e1")
            self.e1.setText(_translate("ListarClientes", "Editar dados"))

            self.d1 = QtWidgets.QPushButton(self.centralwidget)
            self.d1.setGeometry(QtCore.QRect(510, 10, 75, 23))
            self.d1.setObjectName("d1")
            self.d1.setText(_translate("ListarClientes", "Deletar"))

class Janela(QtWidgets.QMainWindow, Ui_ListarClientes):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle('Listar clientes')

if __name__ == '__main__':
    qt = QtWidgets.QApplication([])
    app = Janela()
    app.show()
    sys.exit(qt.exec_())
