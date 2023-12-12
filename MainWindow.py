from PyQt5 import QtWidgets,QtGui,QtCore
import Ui_MainWeiget
import About
import hanoifly
import BasicHanoi

class MainWidget(QtWidgets.QMainWindow,Ui_MainWeiget.Ui_MainWindow):
    def __init__(self):
        super(MainWidget,self).__init__()
        self.setupUi(self)
        self.listDiscs = [self.gray,self.orange,self.yellow,self.green,self.blue]
        self.columnB = []
        self.columnC = []
        self.Disc = [self.listDiscs,self.columnB,self.columnC]
        self.setStartButton()
        self.hanoifly = None
        self.operation = BasicHanoi.hanoi(5,0,1,2)
        self.numberFly = [0]


    def setStartButton(self):
        self.pbAbout.setEnabled(True)
        self.pbExit.setEnabled(True)
        self.pbPause.setEnabled(False)
        self.pbRun.setEnabled(True)
        self.pbReast.setEnabled(True)
        self.pbStep.setEnabled(True)

    def setEndButton(self):
        self.pbAbout.setEnabled(False)
        self.pbExit.setEnabled(False)
        self.pbPause.setEnabled(True)
        self.pbRun.setEnabled(False)
        self.pbReast.setEnabled(False)
        self.pbStep.setEnabled(False)

    
    def on_pbRun_released(self):
        self.hanoifly = hanoifly.hanoifly(self.Disc,self,self.operation,0,self.numberFly)
        self.hanoifly.finished.connect(self.setStartButton)
        self.hanoifly.start()
        self.setEndButton()
    
    def on_pbReast_released(self):
        self.listDiscs = [self.gray,self.orange,self.yellow,self.green,self.blue]
        self.blue.move(21,215)
        self.green.move(21,269)
        self.yellow.move(21,323)
        self.orange.move(21,377)
        self.gray.move(21,431)
        self.columnB = []
        self.columnC = []
        self.tempList = []
        self.setStartButton()
        self.operation = BasicHanoi.hanoi(5,0,1,2)
        self.Disc = [self.listDiscs,self.columnB,self.columnC]
        self.numberFly[0] = 0

    def on_pbPause_released(self):
        self.hanoifly.request()

    def on_pbStep_released(self):
        self.setEndButton()
        self.hanoifly = hanoifly.hanoifly(self.Disc,self,self.operation,1,self.numberFly)
        self.hanoifly.finished.connect(self.setStartButton)
        self.hanoifly.start()

    def on_pbExit_released(self):
            self.close()

    def on_pbAbout_released(self):
        dlg = About.About(self)
        dlg.exec()