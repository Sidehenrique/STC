from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_MainLogin
from Login import *


def main(ui):

    ui.frame_erro.hide()

    def a():
        print(ui.lineEdit.text())
    ui.ENTER.clicked.connect(a)






#
# class MainWindow(QtWidgets.QMainWindow, Ui_MainLogin):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)


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
