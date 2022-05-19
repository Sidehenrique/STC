from PyQt5 import QtWidgets, uic

# FUNÇÕES


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("\PROJETOS\STC\Layout\Display_Login.ui")
primeira_tela.Button_quit.clicked.connetc(self.frame_erro.hide())
primeira_tela.show()



app.exec()


# def funcao_principal():
#     linha1 = Login.lineEdit.text()
#
#     if Login.radioButton.isChecked():
#         print("Música selecionada")
#     elif Login.radioButton_2.isChecked():
#         print("Vídeo selecionado")
#
#     print("ENSIRA UM LINK:", linha1)
#
#
# app = QtWidgets.QApplication([])
# Login = uic.loadUi("Login.ui")
# Login.pushButton_login.clicked.connect(funcao_principal)
#
# app.exec()

