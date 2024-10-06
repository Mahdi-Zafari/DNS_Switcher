from PyQt5 import QtCore, QtGui, QtWidgets
from . import core

class Ui_Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 181)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_top = QtWidgets.QWidget(self.centralwidget)
        self.widget_top.setGeometry(QtCore.QRect(10, 10, 430, 40))
        self.widget_top.setStyleSheet("QWidget{\n"
"    background-color: #202020;\n"
"    border-top-right-radius:13px;\n"
"    border-top-left-radius:13px;\n"
"}")
        self.widget_top.setObjectName("widget_top")
        self.Button_exit = QtWidgets.QPushButton(self.widget_top)
        self.Button_exit.setGeometry(QtCore.QRect(380, 0, 50, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.Button_exit.setFont(font)
        self.Button_exit.setStyleSheet("QPushButton{\n"
"    background-color: #202020;\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:13px;\n"
"    color: #ebe9fc;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:13px;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(170, 0, 0);\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:13px;\n"
"    color: #fff;\n"
"}")
        self.Button_exit.setObjectName("Button_exit")
        self.label_title = QtWidgets.QLabel(self.widget_top)
        self.label_title.setGeometry(QtCore.QRect(40, 10, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: #ebe9fc;")
        self.label_title.setObjectName("label_title")
        self.label_icon = QtWidgets.QLabel(self.widget_top)
        self.label_icon.setGeometry(QtCore.QRect(5, 5, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.label_icon.setFont(font)
        self.label_icon.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap(":/img/img/DNSS_logo.png"))
        self.label_icon.setScaledContents(True)
        self.label_icon.setObjectName("label_icon")
        self.widget_home = QtWidgets.QWidget(self.centralwidget)
        self.widget_home.setGeometry(QtCore.QRect(10, 50, 430, 121))
        self.widget_home.setStyleSheet("QWidget{\n"
"    background-color: #212121;\n"
"    border-bottom-right-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}")
        self.widget_home.setObjectName("widget_home")
        self.widget_option_1 = QtWidgets.QWidget(self.widget_home)
        self.widget_option_1.setGeometry(QtCore.QRect(10, 10, 410, 52))
        self.widget_option_1.setStyleSheet("border: 2px solid #424242;\n"
"border-radius:16px;\n"
"background-color: #212121;")
        self.widget_option_1.setObjectName("widget_option_1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_option_1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_stats = QtWidgets.QLabel(self.widget_option_1)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_stats.setFont(font)
        self.label_stats.setStyleSheet("background-color: none;color: #ebe9fc;border: none;")
        self.label_stats.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stats.setObjectName("label_stats")
        self.gridLayout.addWidget(self.label_stats, 0, 0, 1, 1)
        self.btn_set_or_automatic = QtWidgets.QPushButton(self.widget_home)
        self.btn_set_or_automatic.setGeometry(QtCore.QRect(10, 70, 410, 40))
        self.btn_set_or_automatic.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_set_or_automatic.setFont(font)
        self.btn_set_or_automatic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_set_or_automatic.setStyleSheet("QPushButton{\n"
"    background-color: #3a31d8;\n"
"    border-radius:10px;\n"
"    color: #ebe9fc;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #0600c2;\n"
"border-radius:10px;\n"
"}")
        self.btn_set_or_automatic.setIconSize(QtCore.QSize(30, 30))
        self.btn_set_or_automatic.setObjectName("btn_set_or_automatic")
        self.widget_home.raise_()
        self.widget_top.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_exit.setText(_translate("MainWindow", "×"))
        self.label_title.setText(_translate("MainWindow", "DNS Switcher"))
        self.label_stats.setText(_translate("MainWindow", "Inactive"))
        self.btn_set_or_automatic.setText(_translate("MainWindow", "Set DNS"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
