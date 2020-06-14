from Window.janelaprincipal import Ui_MainWindow
from Window.newclient import Ui_newClientWindow
from Window.listarclientes import Ui_ListarClientes
from Window.login import Ui_TelaLogin
from Window.deletar import Ui_MainWindow3
from Window.registro import Ui_TelaCadastrar
from Window.modifyclient import Ui_modifyClientWindow

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize
import PyQt5.QtCore

import pymysql.cursors

class TelaCadastro(QMainWindow, Ui_TelaCadastrar):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

class JanelaModificarCliente(QMainWindow, Ui_modifyClientWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

class DeletarCliente(QMainWindow, Ui_MainWindow3):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

class JanelaLogin(QMainWindow, Ui_TelaLogin):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnLogin.clicked.connect(self.autentica)
        self.btnCadastrar.clicked.connect(self.telacadastro)
        self.inputSenha.returnPressed.connect(self.autentica)

        self.valido = False

    def autentica(self):
        self.conexao = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='password',
            db='login',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

        with self.conexao.cursor() as c:
            c.execute('SELECT * FROM cadastros')
            resultado = c.fetchall()

        usuario = self.inputUser.text()
        senha = self.inputSenha.text()

        for x in resultado:
            if x['usuario'] == usuario and x['senha'] == senha:
                messagebox = QMessageBox.information(self, 'Sucesso', f'Seja bem vindo, {usuario}')
                self.close()
                self.conexao.close()

                self.main = Principal()
                self.main.show()
                self.valido = True
                break

        if not self.valido:
            messageboxx = QMessageBox.critical(self, 'Erro', 'Usuário ou senha incorretos')

    def telacadastro(self):
        try:
            self.tela = TelaCadastro()
            self.tela.show()

            self.tela.btnCadastrar.clicked.connect(self.cadastrar)

        except Exception as e:
            messageboxxx = QMessageBox.critical(self, 'Erro', f'Erro: {e}')

    def cadastrar(self):
        try:
            self.conexao = pymysql.connect(
                host='127.0.0.1',
                user='root',
                password='password',
                db='login',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

            self.user = self.tela.inputUser.text()
            self.senha = self.tela.inputSenha.text()

            with self.conexao.cursor() as c:
                sql = 'INSERT INTO cadastros VALUES(%s, %s)'
                c.execute(sql, (self.user, self.senha))
                self.conexao.commit()

            essageboxxx = QMessageBox.information(self, 'Erro', f'Cadastro realizado com sucesso!')
            self.conexao.close()
            self.tela.close()

        except Exception as e:
            mess = QMessageBox.critical(self, f'Erro: {e}', 'Erro')

class JanelaListarCliente(QMainWindow, Ui_ListarClientes):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle('Listar clientes')

    def deletar(self):
        pass

class JanelaNovoCliente(QMainWindow, Ui_newClientWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle('Novo cliente')
        self.setWindowIcon(QIcon('addcliente.png'))
        self.setFixedSize(327, 141)

class Principal(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnNovoCliente.setIcon(QIcon(r'addcliente.png'))
        self.btnNovoCliente.setIconSize(QSize(25, 25))
        self.btnNovoCliente.clicked.connect(self.novo_cadastro)

        self.btnListarClientes.setIcon(QIcon('listarclientes.jpg'))
        self.btnListarClientes.setIconSize(QSize(23,23))
        self.btnListarClientes.clicked.connect(self.listar_clientes)
        self.btnListarClientes.clicked.connect(self.atualizar_servicos)

        self.btnAtualizar.clicked.connect(self.atualizar)
        self.btnDelCliente.clicked.connect(self.Janeladeletarcliente)
        self.btnEditarDados.clicked.connect(self.janelaeditardadosID)

        self.tableWidget.setDisabled(True)
        self.tableWidget.setStyleSheet('* {background: #FFF; color: #000;}')

        self.setFixedSize(600,500)
        self.setWindowTitle('Tela principal')

        self.atualizar()

    def atualizar(self):
        self.conexao = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='password',
            db='cadastro2',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

        with self.conexao.cursor() as c:
            _translate = PyQt5.QtCore.QCoreApplication.translate
            try:
                c.execute('SELECT nome, telefone, email FROM clientes')
                resultado = c.fetchall()

                self.tableWidget.setRowCount(0)
                self.tableWidget.setHorizontalHeaderLabels(['Nome', 'Telefone', 'Email'])

                for linha, x in enumerate(resultado):
                    self.tableWidget.insertRow(linha)
                    for coluna, data in enumerate(x.values()):
                        self.tableWidget.setItem(linha, coluna, QTableWidgetItem(str(data)))

                c.execute('SELECT id FROM clientes')
                resultadoid = c.fetchall()

                lista = []
                for x in resultadoid:
                    for c in x.values():
                        lista.append(str(c))

                self.tableWidget.setVerticalHeaderLabels(lista)
            except Exception as e:
                print(e, type(e))

    def Janeladeletarcliente(self):
        try:
            self.dc = DeletarCliente()
            self.dc.show()

            self.dc.btnDeletar.clicked.connect(self.deletarcliente)

        except Exception as e:
            print(e)

    def deletarcliente(self):
        self.conexao = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='password',
            db='cadastro2',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

        id = self.dc.inputId.text()
        try:
            with self.conexao.cursor() as c:
                c.execute(f"DELETE FROM clientes WHERE id = '{id}' ")
                self.conexao.commit()
                messabox = QMessageBox.information(self, 'Sucesso', 'Cliente deletado com sucesso!',)

            self.conexao.close()
            self.dc.close()

        except Exception as e:
            print(e)
            mes = QMessageBox.information(self, 'Erro', 'Não consegui deletar o cliente', )

    def connectdb(self):
        try:
            with self.conexao.cursor() as c:
                nome = self.cw.inputNome.text()
                telefone = self.cw.inputTelefone.text()
                email = self.cw.inputEmail.text()

                if nome == '' or telefone == '' or email == '':
                    messageboxxx = QMessageBox.critical(self, 'Erro', 'Erro: Existem campos vazios')
                    return False

                sql = 'INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)'
                c.execute(sql, (nome, telefone, email))
                messagebox = QMessageBox.information(self, 'Sucesso', 'Cliente cadastro com sucesso.')

            self.conexao.commit()
            self.conexao.close()
            self.cw.close()

        except Exception as e:
            aa = QMessageBox.critical(self, 'ERRO', f'ERRO: {e}\n{type(e)}')

    def janelaeditardadosID(self):
        self.aa = DeletarCliente()
        self.aa.show()

        self.aa.btnDeletar.clicked.connect(self.janelaeditardados)

    def janelaeditardados(self):
        self.conexao = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='password',
            db='cadastro2',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

        self.id = self.aa.inputId.text()
        self.aa.close()

        self.cc = JanelaModificarCliente()
        self.cc.show()
        self.cc.inputIDD.setDisabled(True)
        try:
            with self.conexao.cursor() as c:
                sql = f"SELECT * FROM clientes WHERE id = '{self.id}'"
                c.execute(sql)
                resultado = c.fetchall()
                self.cc.inputIDD.setText(str(resultado[0]['id']))
                self.cc.inputNome.setText(str(resultado[0]['nome']))
                self.cc.inputTelefone.setText(str(resultado[0]['telefone']))
                self.cc.inputEmail.setText(str(resultado[0]['email']))

            self.cc.btnAtualizar.clicked.connect(self.updatetable)

            self.conexao.close()

        except Exception as e:
            msgbox = QMessageBox.critical(self, 'ERRO', f'ERRO: {e}')
            self.cc.close()

    def updatetable(self):
        self.conexao = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='password',
            db='cadastro2',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

        nome = self.cc.inputNome.text()
        telefone = self.cc.inputTelefone.text()
        email = self.cc.inputEmail.text()
        idd = self.cc.inputIDD.text()

        try:
            with self.conexao.cursor() as c:
                sql = f"UPDATE clientes SET nome = '{nome}', telefone = '{telefone}', email = '{email}' WHERE id = '{idd}'"
                c.execute(sql)
                self.conexao.commit()
                msgboxs = QMessageBox.information(self, 'SUCESSO', 'Dados atualizados com sucesso!')
            self.cc.close()
            self.conexao.close()

        except Exception as e:
            msgbox = QMessageBox.critical(self, 'ERRO', f'ERRO: {e}\n{type(e)}')

    def novo_cadastro(self):
        try:
            self.cw = JanelaNovoCliente()
            self.cw.show()

            self.cw.btncadastrar.clicked.connect(self.connectdb)

        except Exception as e:
            print(e)

    def listar_clientes(self):
        try:
            self.lc = JanelaListarCliente()
            self.lc.show()

            self.lc.tableWidget.setDisabled(True)
            self.lc.btnAtualizar.clicked.connect(self.atualizar_servicos)

        except Exception as e:
            print(e)

    def atualizar_servicos(self):
        self.conexao = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='password',
            db='cadastro2',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

        try:
            with self.conexao.cursor() as c:
                c.execute('SELECT c.nome, s.descricao, s.situacao FROM clientes as c JOIN servicos as s ON c.id = s.idcliente')
                resultado = c.fetchall()

                for linha, x in enumerate(resultado):
                    for coluna, data in enumerate(x.values()):
                        self.lc.tableWidget.setItem(linha, coluna, QTableWidgetItem(str(data)))

                c.execute('SELECT clientes.id FROM clientes JOIN servicos ON clientes.id = servicos.idcliente')
                resultadoid = c.fetchall()

                lista = []
                for x in resultadoid:
                    for k in x.values():
                        lista.append(str(k))

                self.lc.tableWidget.setVerticalHeaderLabels(lista)

        except Exception as e:
            mess = QMessageBox.critical(self, 'Erro', f'Erro: {e}')

        self.conexao.close()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = JanelaLogin()
    app.show()
    sys.exit(qt.exec_())
