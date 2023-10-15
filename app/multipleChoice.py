import random
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import multipleChoice_ui
import ods_file

class MultipleChoiceWindowApp(QtWidgets.QMainWindow, multipleChoice_ui.Ui_multipleChoiceWindow):
    def __init__(self, filename, parent=None):
        super(MultipleChoiceWindowApp, self).__init__(parent)
        self.setupUi(self)
        self.filename = filename
        self.Score = 0
        self.Attempts = 0
        self.dataset = ods_file.ods_data(self.filename)
        self.loadGuesses()
        self.quitButton.clicked.connect(self.closeWindow)
        self.checkButton.clicked.connect(self.checkAnswer)
        self.englishToGermanRadioButton.toggled.connect(self.loadGuesses)
        self.attemptsLabel.setText(str(self.Attempts))
        self.scoreLabel.setText(str(self.Score))
        self.correctLabel.setText("Viel Spass!")

    def checkAnswer(self):
        correct_incorrect = 0
        self.Attempts = self.Attempts + 1
        if(self.guessRadioButton1.isChecked()):
            if(self.guessRadioButton1.text() == self.controlAns):
                self.Score = self.Score + 1
                correct_incorrect = 1
            else:
                self.Score = self.Score - 1
                correct_incorrect = 0
        elif(self.guessRadioButton2.isChecked()):
            if (self.guessRadioButton2.text() == self.controlAns):
                self.Score = self.Score + 1
                correct_incorrect = 1
            else:
                self.Score = self.Score - 1
                correct_incorrect = 0
        elif(self.guessRadioButton3.isChecked()):
            if (self.guessRadioButton3.text() == self.controlAns):
                self.Score = self.Score + 1
                correct_incorrect = 1
            else:
                self.Score = self.Score - 1
                correct_incorrect = 0
        elif(self.guessRadioButton4.isChecked()):
            if (self.guessRadioButton4.text() == self.controlAns):
                self.Score = self.Score + 1
                correct_incorrect = 1
            else:
                self.Score = self.Score - 1
                correct_incorrect = 0
        elif(self.guessRadioButton5.isChecked()):
            if (self.guessRadioButton5.text() == self.controlAns):
                self.Score = self.Score + 1
                correct_incorrect = 1
            else:
                self.Score = self.Score - 1
                correct_incorrect = 0
        else:
            self.Score = self.Score
        self.scoreLabel.setText(str(self.Score))
        self.attemptsLabel.setText(str(self.Attempts))
        if(correct_incorrect == 1):
            self.correctLabel.setText("<p style='color:green'>Sehr Gut!<\p>")
        else:
            self.correctLabel.setText("<p style='color:red'>Falsh. Dummkopf!<\p>")
        QtCore.QCoreApplication.processEvents()
        time.sleep(1)
        self.correctLabel.setText("")
        self.loadGuesses()


    def loadGuesses(self):
        self.currentGuesses = self.dataset.getSubsetList()
        z = random.randint(0,4)
        ansIndex = []

        self.clearRadioButtons()
        for x in range(len(self.currentGuesses)):
            if(type(self.currentGuesses[x][0]) == float):
                self.currentGuesses[x][0] = self.currentGuesses[x][1]

        if(self.englishToGermanRadioButton.isChecked()):
            self.controlWord = self.currentGuesses[0][0]
            self.controlAns = str(self.currentGuesses[0][2])
            for x in range(5):
                y = (x+z+1)%5
                ansIndex.append(y)
            self.guessRadioButton1.setText(str(self.currentGuesses[ansIndex[0]][2]))
            self.guessRadioButton2.setText(str(self.currentGuesses[ansIndex[1]][2]))
            self.guessRadioButton3.setText(str(self.currentGuesses[ansIndex[2]][2]))
            self.guessRadioButton4.setText(str(self.currentGuesses[ansIndex[3]][2]))
            self.guessRadioButton5.setText(str(self.currentGuesses[ansIndex[4]][2]))
        else:
            self.controlWord = self.currentGuesses[0][2]
            self.controlAns = self.currentGuesses[0][0]
            for x in range(5):
                y = (x+z+1)%5
                ansIndex.append(y)
            self.guessRadioButton1.setText(str(self.currentGuesses[ansIndex[0]][0]))
            self.guessRadioButton2.setText(str(self.currentGuesses[ansIndex[1]][0]))
            self.guessRadioButton3.setText(str(self.currentGuesses[ansIndex[2]][0]))
            self.guessRadioButton4.setText(str(self.currentGuesses[ansIndex[3]][0]))
            self.guessRadioButton5.setText(str(self.currentGuesses[ansIndex[4]][0]))
        self.ControlWordLabel.setText(str(self.controlWord))

    def closeWindow(self):
        self.close()

    def clearRadioButtons(self):
        self.buttonGroup_guess_text.setExclusive(False)
        self.guessRadioButton1.setChecked(False)
        self.guessRadioButton2.setChecked(False)
        self.guessRadioButton3.setChecked(False)
        self.guessRadioButton4.setChecked(False)
        self.guessRadioButton5.setChecked(False)
        self.buttonGroup_guess_text.setExclusive(True)