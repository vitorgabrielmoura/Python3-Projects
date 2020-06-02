# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaCadastrar(object):
    def setupUi(self, TelaCadastrar):
        TelaCadastrar.setObjectName("TelaCadastrar")
        TelaCadastrar.resize(324, 274)
        TelaCadastrar.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(TelaCadastrar)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Counter-Strike")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.inputUser = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUser.setGeometry(QtCore.QRect(60, 110, 211, 31))
        self.inputUser.setObjectName("inputUser")
        self.inputSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.inputSenha.setGeometry(QtCore.QRect(60, 170, 211, 31))
        self.inputSenha.setObjectName("inputSenha")
        self.inputSenha.setEchoMode(QtWidgets.QLineEdit.Password)

        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(110, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setObjectName("btnCadastrar")
        TelaCadastrar.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaCadastrar)
        QtCore.QMetaObject.connectSlotsByName(TelaCadastrar)

    def retranslateUi(self, TelaCadastrar):
        _translate = QtCore.QCoreApplication.translate
        TelaCadastrar.setWindowTitle(_translate("TelaCadastrar", "Login"))
        self.label.setText(_translate("TelaCadastrar", "REGISTRO"))
        self.label_2.setText(_translate("TelaCadastrar", "Usuário"))
        self.label_3.setText(_translate("TelaCadastrar", "Senha"))
        self.btnCadastrar.setText(_translate("TelaCadastrar", "Cadastrar"))
