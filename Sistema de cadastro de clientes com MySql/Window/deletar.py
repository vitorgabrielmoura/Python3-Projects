# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bda3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(100, 100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputId = QtWidgets.QLineEdit(self.centralwidget)
        self.inputId.setGeometry(QtCore.QRect(20, 40, 61, 20))
        self.inputId.setObjectName("inputId")
        self.btnDeletar = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeletar.setGeometry(QtCore.QRect(30, 70, 41, 23))
        self.btnDeletar.setObjectName("btnDeletar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 11, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 104, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnDeletar.setText(_translate("MainWindow", "Ok"))
        self.label_2.setText(_translate("MainWindow", "Digite o Id"))

