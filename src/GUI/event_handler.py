from PyQt5 import QtCore, QtGui, QtWidgets


class EventHandler():

    def __init__(self):
        pass

    def search_button_on_click(self, search_button: QtWidgets.QPushButton):
        print(1)
        search_button.setText('clicked')


