# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\exercise\homework\hanoi\About.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(700, 500)
        self.listView = QtWidgets.QListView(About)
        self.listView.setGeometry(QtCore.QRect(0, 0, 700, 500))
        self.listView.setStyleSheet("background-image: url(:/newPrefix/resource/wallhaven-ey2rmk.jpg);")
        self.listView.setObjectName("listView")
        self.textBrowser = QtWidgets.QTextBrowser(About)
        self.textBrowser.setGeometry(QtCore.QRect(110, 20, 461, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.pbClose = QtWidgets.QPushButton(About)
        self.pbClose.setGeometry(QtCore.QRect(500, 370, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pbClose.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/resource/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pbClose.setIcon(icon)
        self.pbClose.setIconSize(QtCore.QSize(40, 40))
        self.pbClose.setObjectName("pbClose")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Dialog"))
        self.textBrowser.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">About This Software!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  The software was developed under the guidance of Alex from Chongqing University.The producer is Zhuo Zhao, a class 3 2019 student in the computer science department.Thank you for your playing.</span></p></body></html>"))
        self.pbClose.setText(_translate("About", "Exit"))
import images_rc
