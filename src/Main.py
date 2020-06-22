import sys
from PyQt5 import QtWidgets, uic

from MainWindow import Ui_MainWindow
from EventHandler import EventHandler


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
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

