from PyQt5 import QtCore, QtGui, QtWidgets
import mainwindow_ui
import multipleChoice
import derdieoderdas
import ods_file

class MainWindowApp(QtWidgets.QMainWindow, mainwindow_ui.Ui_MainWindow):
    def __init__(self, filename, parent=None):
        super(MainWindowApp, self).__init__(parent)
        self.setupUi(self)
        self.filename = filename
        self.exitButton.clicked.connect(self.closeWindow)
        self.playButton.clicked.connect(self.playButtonClicked)
        self.multipleChoiceGameRadioButton.setHidden(False)
        self.matchThePicRadioButton.setHidden(True)
        self.derDieOderDasRadioButton.setHidden(False)

    def closeWindow(self):
        QtCore.QCoreApplication.quit()

    def playButtonClicked(self):

        if(self.multipleChoiceGameRadioButton.isChecked()):
                self.multChoiceWindow = multipleChoice.MultipleChoiceWindowApp(self.filename)
                self.multChoiceWindow.show()
        elif(self.derDieOderDasRadioButton.isChecked()):
                self.derDieOderDasWindow = derdieoderdas.derDieOderDasWindowApp(self.filename)
                self.derDieOderDasWindow.show()
        elif(self.matchThePicRadioButton.isChecked()):
                print(f'Match the picture radio button checked...')