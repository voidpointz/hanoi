from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5 import QtWidgets
import BasicHanoi
import BasicHanoi
import time

class hanoifly(QThread):
    updateInformer = pyqtSignal()
    def __init__(self,disc,parent,operation,iId,numberFly):
        super().__init__(parent)
        self.columnA = disc[0]
        self.columnB = disc[1]
        self.columnC = disc[2]
        self.terminate = False
        self.operation = operation
        self.iId = iId
        self.numberFly = numberFly


    def request(self):
        self.terminate = True

    def run(self):
        if self.iId == 0:
            while self.operation:
                self.numberFly[0] += 1
                if self.terminate:
                    break
                x,y = next(self.operation)
                self.plateJudge(x,y)
                if self.numberFly[0] == 31:
                    break
        else:
            x,y = next(self.operation)
            self.plateJudge(x,y)
            self.numberFly[0] += 1


    def plateJudge(self,x,y):
        
        if x == 0 and y == 1:
            self.flyPlate(self.columnA,self.columnB,21,21+330)
        elif x == 0 and y == 2:
            self.flyPlate(self.columnA,self.columnC,21,21+330*2)
        elif x == 1 and y == 0:
            self.flyPlate(self.columnB,self.columnA,21+330,21)
        elif x == 1 and y == 2:
            self.flyPlate(self.columnB,self.columnC,21+330,21+330*2)
        elif x == 2 and y == 0:
            self.flyPlate(self.columnC,self.columnA,21+330*2,21)
        elif x == 2 and y == 1:
            self.flyPlate(self.columnC,self.columnB,21+330*2,21+330)

    def flyPlate(self,columnStart,columnEnd,wideStart,wideEnd):
        speed = 0.001
        tempPlate = columnStart.pop()
        columnEnd.append(tempPlate)
        highend = len(columnEnd)
        highend = 431 - (highend-1)*54
        highStart = 431 - len(columnStart)*54
        x,y,z = highStart,wideStart,100
        while x > 100:
            x -= speed
            tempPlate.move(wideStart,x)
        if y < wideEnd:
            while y < wideEnd:
                y += speed
                tempPlate.move(y,100)
        else:
            while y > wideEnd:
                y -= speed
                tempPlate.move(y,100)
        while z < highend:
            z += speed
            tempPlate.move(wideEnd,z)
        print(columnStart,columnEnd,wideStart,wideEnd)
