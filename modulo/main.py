from Login import *
from Home import *
import mod


def main(ui):
    # Tratamento do POPUP -----------------------------------------------------------------
    ui.frame_erro.hide()
    ui.Button_quit.clicked.connect(lambda: ui.frame_erro.hide())

    def mensage(mensagem):
        ui.frame_erro.show()
        ui.label_erro.setText(mensagem)

    # VALIDAÇÃO DE DADOS -----------------------------------------------------------------
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
            texto1 = 'Usuário ou senha incorreto'
            mensage(texto1)
            return

        if password == senha_bd[0][0]:
            texto2 = 'Login efetuado com sucesso'
            mensage(texto2)
            print('Sucesso!!!')
            MainLogin.close()
            MainWindow.show()

        else:
            texto3 = 'A senha esta incorreta'
            mensage(texto3)

    ui.ENTER.clicked.connect(checkPassword)


def home(mw):
    # Tratamento Botão sair -----------------------------------------------------------
    def getLogin():
        MainWindow.close()
        MainLogin.show()
    mw.pushButton_sair.clicked.connect(getLogin)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainLogin = QtWidgets.QMainWindow()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainLogin()
    mw = Ui_MainWindow()
    mw.setupUi(MainWindow)
    ui.setupUi(MainLogin)
    MainLogin.show()
    main(ui)
    home(mw)
    sys.exit(app.exec_())
