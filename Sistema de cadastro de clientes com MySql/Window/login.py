# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        TelaLogin.setObjectName("TelaLogin")
        TelaLogin.resize(360, 301)
        TelaLogin.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.centralwidget = QtWidgets.QWidget(TelaLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Counter-Strike")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.inputSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.inputSenha.setGeometry(QtCore.QRect(70, 190, 211, 31))
        self.inputSenha.setText("")
        self.inputSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputSenha.setObjectName("inputSenha")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(70, 240, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(180, 240, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.inputUser = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUser.setGeometry(QtCore.QRect(70, 130, 211, 31))
        self.inputUser.setStyleSheet("border-color: rgb(0, 85, 255);")
        self.inputUser.setObjectName("inputUser")
        self.inputUser.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.inputSenha.raise_()
        self.btnLogin.raise_()
        self.btnCadastrar.raise_()
        TelaLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaLogin)
        QtCore.QMetaObject.connectSlotsByName(TelaLogin)

    def retranslateUi(self, TelaLogin):
        _translate = QtCore.QCoreApplication.translate
        TelaLogin.setWindowTitle(_translate("TelaLogin", "Login"))
        self.label.setText(_translate("TelaLogin", "SISTEMA DE \n"
"CADASTROS"))
        self.label_2.setText(_translate("TelaLogin", "Usuário"))
        self.label_3.setText(_translate("TelaLogin", "Senha"))
        self.btnLogin.setText(_translate("TelaLogin", "Login"))
        self.btnCadastrar.setText(_translate("TelaLogin", "Cadastrar"))
