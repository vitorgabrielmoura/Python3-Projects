# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'validador.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(164, 217)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnValidarCpf = QtWidgets.QPushButton(self.centralwidget)
        self.btnValidarCpf.setGeometry(QtCore.QRect(30, 80, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnValidarCpf.setFont(font)
        self.btnValidarCpf.setObjectName("btnValidarCpf")
        self.inputCPF = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCPF.setGeometry(QtCore.QRect(10, 50, 141, 20))
        self.inputCPF.setText("")
        self.inputCPF.setObjectName("inputCPF")
        self.btnGerarCpf = QtWidgets.QPushButton(self.centralwidget)
        self.btnGerarCpf.setGeometry(QtCore.QRect(30, 170, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnGerarCpf.setFont(font)
        self.btnGerarCpf.setObjectName("btnGerarCpf")
        self.lineCPFgerador = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCPFgerador.setGeometry(QtCore.QRect(10, 120, 141, 20))
        self.lineCPFgerador.setText("")
        self.lineCPFgerador.setObjectName("lineCPFgerador")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 200, 47, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 200, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.selectPontuacao = QtWidgets.QCheckBox(self.centralwidget)
        self.selectPontuacao.setGeometry(QtCore.QRect(10, 140, 70, 17))
        self.selectPontuacao.setObjectName("selectPontuacao")
        self.selectCopiar = QtWidgets.QCheckBox(self.centralwidget)
        self.selectCopiar.setGeometry(QtCore.QRect(90, 140, 51, 17))
        self.selectCopiar.setObjectName("selectCopiar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnValidarCpf.setText(_translate("MainWindow", "Validar CPF"))
        self.inputCPF.setPlaceholderText(_translate("MainWindow", "Ex: 352.111.480-53 "))
        self.btnGerarCpf.setText(_translate("MainWindow", "Gerar CPF"))
        self.lineCPFgerador.setPlaceholderText(_translate("MainWindow", "Seu CPF será gerado aqui!"))
        self.label.setText(_translate("MainWindow", "Gerador/Validador CPF"))
        self.label_3.setText(_translate("MainWindow", "Made by Vitu"))
        self.selectPontuacao.setText(_translate("MainWindow", "Pontuação"))
        self.selectCopiar.setText(_translate("MainWindow", "Copiar"))
