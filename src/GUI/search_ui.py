# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from event_handler import EventHandler


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchLabel.setFont(font)
        self.searchLabel.setObjectName("searchLabel")
        self.gridLayout_2.addWidget(self.searchLabel, 0, 0, 1, 1)
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.gridLayout_2.addWidget(self.searchLineEdit, 0, 1, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.searchButton, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.searchTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.searchTableWidget.setObjectName("searchTableWidget")
        self.searchTableWidget.setColumnCount(0)
        self.searchTableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.searchTableWidget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.previousButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.previousButton.setFont(font)
        self.previousButton.setObjectName("previousButton")
        self.gridLayout.addWidget(self.previousButton, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.playpauseButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.playpauseButton.setFont(font)
        self.playpauseButton.setObjectName("playpauseButton")
        self.gridLayout.addWidget(self.playpauseButton, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.gridLayout)
        self.elapsedTimeSlider = QtWidgets.QSlider(self.centralwidget)
        self.elapsedTimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.elapsedTimeSlider.setObjectName("elapsedTimeSlider")
        self.verticalLayout.addWidget(self.elapsedTimeSlider)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setup_signal()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchLabel.setText(_translate("MainWindow", "Search:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.previousButton.setText(_translate("MainWindow", "Previous"))
        self.playpauseButton.setText(_translate("MainWindow", "Play/Pause"))
        self.nextButton.setText(_translate("MainWindow", "Next"))

    def setup_signal(self):
        event = EventHandler()
        self.searchButton.clicked.connect(lambda: event.search_button_on_click(
            self.searchButton
        ))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
