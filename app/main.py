from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import MainWindowApp
from PyQt5.QtWidgets import QApplication
import sys

filename = '../vocabulary.ods'
def main():
    app = QApplication(sys.argv)
    form = MainWindowApp(filename)
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()