from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

from auth import *

class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.enter_button.clicked.connect(self.Enter)       
        self.ui.author_bottin.clicked.connect(self.About)
               

    def Enter(self):
        log=(self.ui.login_edit.text()=="admin")
        pas=(self.ui.pass_edit.text()=="admin")
        if (log and pas == True):
            self.ui.login.setVisible(False)
            self.ui.password.setVisible(False)
            self.ui.login_edit.setVisible(False)
            self.ui.pass_edit.setVisible(False)
            self.ui.is_success.setVisible(True)
            self.ui.enter_button.setText("Выйти")
            self.ui.enter_button.clicked.connect(self.Out)
        elif (log == False):
            QMessageBox.about(self, "Error login", "Ask the administrator for the login and try to enter again")
        elif (pas == False):
            QMessageBox.about(self, "Error password", "Ask the administrator for the password and try to enter again")
        else:
            QMessageBox.about(self, "Unexpected error", "Reboot and try again")

    def Out(self):
        self.ui.is_success.setVisible(False)
        self.ui.login.setVisible(True)
        self.ui.password.setVisible(True)
        self.ui.login_edit.setVisible(True)
        self.ui.pass_edit.setVisible(True)
        self.ui.enter_button.setText("Войти")
        self.ui.enter_button.clicked.connect(self.Enter)

    def About(self):
        QMessageBox.about(self, "Information about author", "student of BMSTU, group - IUK4-31B \nOtroshenko Taisia")


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

