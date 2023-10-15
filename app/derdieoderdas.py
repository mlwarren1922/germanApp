from PyQt5 import QtCore, QtGui, QtWidgets
import derdieoderdas_ui
import ods_file

class derDieOderDasWindowApp(QtWidgets.QMainWindow, derdieoderdas_ui.Ui_derDieOderDasWindow):
    def __init__(self, filename, parent=None):
        super(derDieOderDasWindowApp, self).__init__(parent)
        self.setupUi(self)
        self.filename = filename
        self.Score = 0
        self.Attempts = 0
        self.dataset = ods_file.ods_data(self.filename)
        self.quitButton.clicked.connect(self.closeWindow)
        self.checkButton.clicked.connect(self.checkAnswer)
        self.attemptsLabel.setText(str(self.Attempts))
        self.scoreLabel.setText(str(self.Score))
        self.correctLabel.setText("Viel Spass!")
        self.loadGuess()

    def loadGuess(self):
        self.currentGuess = self.dataset.getSingleLine()
        print(f"{self.currentGuess[0][0]}")

    def checkAnswer(self):
        print(f"check answer")

    def closeWindow(self):
        self.close()
