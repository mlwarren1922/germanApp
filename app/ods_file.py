import pandas as pd
import odf.opendocument
import random

class ods_data():
    def __init__(self,filename):
        print(f'Working with vocabulary in {filename}...')
        self.filename = filename
        self.data = pd.read_excel(filename)

    def getData(self):
        return self.data

    def getSubsetList(self):
        self.vocabArray = []
        numberOfRows = len(self.data)
        for x in range(5):
            self.vocabArray.append(self.data.iloc[random.randint(0, numberOfRows-1)].tolist())
        return self.vocabArray

    def getSingleLine(self):
        self.vocabArray = []
        numberOfRows = len(self.data)
        self.vocabArray.append(self.data.iloc[random.randint(0,numberOfRows-1)].tolist())
        return self.vocabArray
