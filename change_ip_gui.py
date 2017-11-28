import wmi
import os
import ccav
import sys
import ccav
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox

if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ccav.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

