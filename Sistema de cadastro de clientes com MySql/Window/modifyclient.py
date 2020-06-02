# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifyclient.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modifyClientWindow(object):
    def setupUi(self, modifyClientWindow):
        modifyClientWindow.setObjectName("modifyClientWindow")
        modifyClientWindow.resize(327, 141)
        modifyClientWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(modifyClientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.label.setObjectName("label")
        self.inputNome = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNome.setGeometry(QtCore.QRect(10, 30, 241, 20))
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
        self.btnAtualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtualizar.setGeometry(QtCore.QRect(120, 110, 75, 23))
        self.btnAtualizar.setObjectName("btnAtualizar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 10, 31, 16))
        self.label_4.setObjectName("label_4")
        self.inputIDD = QtWidgets.QLineEdit(self.centralwidget)
        self.inputIDD.setGeometry(QtCore.QRect(260, 30, 51, 20))
        self.inputIDD.setObjectName("inputIDD")
        modifyClientWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(modifyClientWindow)
        QtCore.QMetaObject.connectSlotsByName(modifyClientWindow)

    def retranslateUi(self, modifyClientWindow):
        _translate = QtCore.QCoreApplication.translate
        modifyClientWindow.setWindowTitle(_translate("modifyClientWindow", "MainWindow"))
        self.label.setText(_translate("modifyClientWindow", "Nome:"))
        self.label_2.setText(_translate("modifyClientWindow", "Telefone:"))
        self.inputTelefone.setPlaceholderText(_translate("modifyClientWindow", "(11) 95964 - 0720"))
        self.label_3.setText(_translate("modifyClientWindow", "E-mail:"))
        self.btnAtualizar.setText(_translate("modifyClientWindow", "Atualizar"))
        self.label_4.setText(_translate("modifyClientWindow", "Id"))
