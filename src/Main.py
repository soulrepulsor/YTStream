import sys
from PyQt5 import QtWidgets, uic

from MainWindow import Ui_MainWindow
from EventHandler import EventHandler

class Login(QtWidgets.QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.setWindowTitle("Login")
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handle_login)
        self.buttonRegister = QtWidgets.QPushButton('Register', self)
        self.buttonRegister.clicked.connect(self.handle_register)
        layout = QtWidgets.QFormLayout(self)
        layout.setContentsMargins(10,10,10,10)
        layout.setSpacing(10)
        layout.addRow(QtWidgets.QLabel("Username:"), self.textName)
        layout.addRow(QtWidgets.QLabel("Password:"), self.textPass)
        layout.addRow(self.buttonLogin, self.buttonRegister)

    def handle_login(self):
        if (self.textName.text() == 'foo' and
                self.textPass.text() == 'bar'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

    def handle_register(self):
        pass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setup_signal()

    def setup_signal(self):
        handler = EventHandler()
        self.searchButton.clicked.connect(
            lambda: handler.search_button_onclicked(
                self.searchLineEdit.text(), self.searchTableView
            )
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # main = MainWindow()
    # main.show()
    # sys.exit(app.exec_())
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
