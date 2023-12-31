# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\exercise\homework\hanoi\MainWeiget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 480, 911, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalLayoutWidget.sizePolicy().hasHeightForWidth())
        self.horizontalLayoutWidget.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbRun = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pbRun.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbRun.sizePolicy().hasHeightForWidth())
        self.pbRun.setSizePolicy(sizePolicy)
        self.pbRun.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pbRun.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/resource/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pbRun.setIcon(icon)
        self.pbRun.setIconSize(QtCore.QSize(48, 48))
        self.pbRun.setObjectName("pbRun")
        self.horizontalLayout.addWidget(self.pbRun)
        self.pbReast = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbReast.sizePolicy().hasHeightForWidth())
        self.pbReast.setSizePolicy(sizePolicy)
        self.pbReast.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pbReast.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/resource/reast.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pbReast.setIcon(icon1)
        self.pbReast.setIconSize(QtCore.QSize(48, 48))
        self.pbReast.setObjectName("pbReast")
        self.horizontalLayout.addWidget(self.pbReast)
        self.pbStep = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbStep.sizePolicy().hasHeightForWidth())
        self.pbStep.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pbStep.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/resource/step.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pbStep.setIcon(icon2)
        self.pbStep.setIconSize(QtCore.QSize(48, 48))
        self.pbStep.setObjectName("pbStep")
        self.horizontalLayout.addWidget(self.pbStep)
        self.pbPause = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbPause.sizePolicy().hasHeightForWidth())
        self.pbPause.setSizePolicy(sizePolicy)
        self.pbPause.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pbPause.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/resource/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pbPause.setIcon(icon3)
        self.pbPause.setIconSize(QtCore.QSize(48, 48))
        self.pbPause.setObjectName("pbPause")
        self.horizontalLayout.addWidget(self.pbPause)
        self.pbExit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbExit.sizePolicy().hasHeightForWidth())
        self.pbExit.setSizePolicy(sizePolicy)
        self.pbExit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pbExit.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/resource/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pbExit.setIcon(icon4)
        self.pbExit.setIconSize(QtCore.QSize(48, 48))
        self.pbExit.setObjectName("pbExit")
        self.horizontalLayout.addWidget(self.pbExit)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.listView.setStyleSheet("border-image: url(:/newPrefix/resource/background.png);")
        self.listView.setObjectName("listView")
        self.pbAbout = QtWidgets.QPushButton(self.centralwidget)
        self.pbAbout.setGeometry(QtCore.QRect(910, 0, 51, 51))
        self.pbAbout.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/resource/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pbAbout.setIcon(icon5)
        self.pbAbout.setIconSize(QtCore.QSize(35, 35))
        self.pbAbout.setObjectName("pbAbout")
        self.blue = QtWidgets.QPushButton(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(21, 231, 250, 50))
        self.blue.setMinimumSize(QtCore.QSize(250, 50))
        self.blue.setStyleSheet("border-image: url(:/newPrefix/resource/blue.png);")
        self.blue.setText("")
        self.blue.setObjectName("blue")
        self.green = QtWidgets.QPushButton(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(21, 281, 250, 50))
        self.green.setMinimumSize(QtCore.QSize(250, 50))
        self.green.setStyleSheet("border-image: url(:/newPrefix/resource/green.png);")
        self.green.setText("")
        self.green.setObjectName("green")
        self.yellow = QtWidgets.QPushButton(self.centralwidget)
        self.yellow.setGeometry(QtCore.QRect(21, 331, 250, 50))
        self.yellow.setMinimumSize(QtCore.QSize(250, 50))
        self.yellow.setStyleSheet("border-image: url(:/newPrefix/resource/yellow.png);")
        self.yellow.setText("")
        self.yellow.setObjectName("yellow")
        self.orange = QtWidgets.QPushButton(self.centralwidget)
        self.orange.setGeometry(QtCore.QRect(21, 381, 250, 50))
        self.orange.setMinimumSize(QtCore.QSize(250, 50))
        self.orange.setStyleSheet("border-image: url(:/newPrefix/resource/orange.png);")
        self.orange.setText("")
        self.orange.setObjectName("orange")
        self.gray = QtWidgets.QPushButton(self.centralwidget)
        self.gray.setGeometry(QtCore.QRect(21, 431, 250, 50))
        self.gray.setMinimumSize(QtCore.QSize(250, 50))
        self.gray.setStyleSheet("border-image: url(:/newPrefix/resource/gray.png);")
        self.gray.setText("")
        self.gray.setObjectName("gray")
        self.listView.raise_()
        self.horizontalLayoutWidget.raise_()
        self.pbAbout.raise_()
        self.blue.raise_()
        self.green.raise_()
        self.yellow.raise_()
        self.orange.raise_()
        self.gray.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hanoi"))
        self.pbRun.setText(_translate("MainWindow", "Run"))
        self.pbReast.setText(_translate("MainWindow", "Reast"))
        self.pbStep.setText(_translate("MainWindow", "step"))
        self.pbPause.setText(_translate("MainWindow", "Pause"))
        self.pbExit.setText(_translate("MainWindow", "Exit"))
import images_rc
