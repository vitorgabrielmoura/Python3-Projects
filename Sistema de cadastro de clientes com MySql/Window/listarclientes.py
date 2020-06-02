# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listarclientes.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListarClientes(object):
    def setupUi(self, ListarClientes):
        ListarClientes.setObjectName("ListarClientes")
        ListarClientes.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(ListarClientes)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 561, 411))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(181)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(37)
        self.tableWidget.verticalHeader().setMinimumSectionSize(37)
        self.brnEditarDados = QtWidgets.QPushButton(self.centralwidget)
        self.brnEditarDados.setGeometry(QtCore.QRect(150, 440, 101, 31))
        self.brnEditarDados.setObjectName("brnEditarDados")
        self.btnFiltrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnFiltrar.setGeometry(QtCore.QRect(490, 440, 91, 31))
        self.btnFiltrar.setObjectName("btnFiltrar")
        self.btnAtualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAtualizar.setGeometry(QtCore.QRect(20, 440, 101, 31))
        self.btnAtualizar.setObjectName("btnAtualizar")
        self.inputFiltrar = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFiltrar.setGeometry(QtCore.QRect(330, 440, 151, 31))
        self.inputFiltrar.setObjectName("inputFiltrar")
        ListarClientes.setCentralWidget(self.centralwidget)

        self.retranslateUi(ListarClientes)
        QtCore.QMetaObject.connectSlotsByName(ListarClientes)

    def retranslateUi(self, ListarClientes):
        _translate = QtCore.QCoreApplication.translate
        ListarClientes.setWindowTitle(_translate("ListarClientes", "ListarClientes"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ListarClientes", "Cliente"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ListarClientes", "Descrição"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ListarClientes", "Situação"))
        self.brnEditarDados.setText(_translate("ListarClientes", "Editar"))
        self.btnFiltrar.setText(_translate("ListarClientes", "Filtrar"))
        self.btnAtualizar.setText(_translate("ListarClientes", "Atualizar"))
        self.inputFiltrar.setPlaceholderText(_translate("ListarClientes", "Digite o id/nome do cliente"))
