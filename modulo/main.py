import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_MainLogin
from Login import *
import mod


def main(ui):
    # Tratamento do POPUP
    ui.frame_erro.hide()
    ui.Button_quit.clicked.connect(lambda: ui.frame_erro.hide())

    def checkPassword():
        usuario = ui.lineEdit.text()
        password = ui.lineEdit_3.text()
        print(usuario, password)

        try:
            cursor = mod.conectar_mssql()
            cursor.execute(f"""SELECT senha FROM cadastro WHERE usuario = '{usuario}';""")
            senha_bd = cursor.fetchall()
            print(senha_bd[0][0])
            cursor.close()

        except:
            print('Usuário ou senha incorreto')
            return

        if password == senha_bd[0][0]:
            print('Sucesso!!!')

        else:
            print('Senha incorreta')

    ui.ENTER.clicked.connect(checkPassword)


# def checkPassword():
#     usuario = usuario
#     password = password
#
#     try:
#         cursor = mod.conectar_mssql()
#         cursor.execute(f"""SELECT senha FROM cadastro WHERE usuario = '{usuario}';""")
#         senha_bd = cursor.fetchall()
#         print(senha_bd[0][0])
#         cursor.close()
#
#     except:
#         print('usuario ou senha invalidos')
#
#     if password == senha_bd[0][0]:
#         print('Home')
#
#


# Usuario e Senha
# User = ui.lineEdit.text()
# Password = ui.lineEdit_3.text()
#
#
# ui.ENTER.clicked.connect()
#
#
# def checkPassword(User, Password):
#     textUser = ''
#     textPassword = ''
#
#     if textUser and textPassword != '':
#         print('Usuário ou Senha invalido')


# def checkFields(self):
#     textUser = ''
#     textPassword = ''
#
#     def showMessage(message):
#         self.frame_erro.show()
#         self.label_erro.setText(message)
#
#     # CHECAR USUÁRIO
#     if not self.lineEdit.text():
#         textUser = ' User Empyt. '
#     else:
#         textUser = ''
#
#     # CHECAR PASSWORD
#     if not self.lineEdit_3.text():
#         textPassword = ' Password Empyt. '
#     else:
#         textPassword = ''
#
#     # CHECK FIELDS
#     if textUser + textPassword != '':
#         text = textUser + textPassword
#         showMessage(text)
#     else:
#         text = ' Login OK. '
#         if self.checkBox.isChecked():
#             text = text + ' | Saver user: OK '
#         showMessage(text)
#
#     # POPUP BUTTON
#     self.Button_quit.clicked.connect(lambda: self.frame_erro.hide())
#
#     # INICIAR POPUP OCULTAMENTE
#     self.frame_erro.hide()
#
#     # BUTTON LOGIN
#     self.ENTER.clicked.connect(self.checkFields)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainLogin = QtWidgets.QMainWindow()
    ui = Ui_MainLogin()
    ui.setupUi(MainLogin)
    MainLogin.show()
    main(ui)
    sys.exit(app.exec_())
