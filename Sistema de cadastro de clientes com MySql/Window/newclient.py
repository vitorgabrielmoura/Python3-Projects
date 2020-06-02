# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newclient.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newClientWindow(object):
    def setupUi(self, newClientWindow):
        newClientWindow.setObjectName("newClientWindow")
        newClientWindow.resize(327, 141)
        newClientWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(newClientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.label.setObjectName("label")
        self.inputNome = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNome.setGeometry(QtCore.QRect(10, 30, 311, 20))
        self.inputNome.setObjectName("inputNome")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.inputTelefone = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTelefone.setGeometry(QtCore.QRect(10, 80, 111, 20))
        self.inputTelefone.setObjectName("inputTelefone")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.inputEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEmail.setGeometry(QtCore.QRect(130, 80, 191, 20))
        self.inputEmail.setText("")
        self.inputEmail.setObjectName("inputEmail")
        self.btncadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btncadastrar.setGeometry(QtCore.QRect(120, 110, 75, 23))
        self.btncadastrar.setObjectName("btncadastrar")
        newClientWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(newClientWindow)
        QtCore.QMetaObject.connectSlotsByName(newClientWindow)

    def retranslateUi(self, newClientWindow):
        _translate = QtCore.QCoreApplication.translate
        newClientWindow.setWindowTitle(_translate("newClientWindow", "MainWindow"))
        self.label.setText(_translate("newClientWindow", "Nome:"))
        self.label_2.setText(_translate("newClientWindow", "Telefone:"))
        self.inputTelefone.setPlaceholderText(_translate("newClientWindow", "(11) 95964 - 0720"))
        self.label_3.setText(_translate("newClientWindow", "E-mail:"))
        self.btncadastrar.setText(_translate("newClientWindow", "Cadastrar"))
