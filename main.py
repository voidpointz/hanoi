import sys
from PyQt5 import QtWidgets
from MainWindow import MainWidget
from bgm import Bgm

app = QtWidgets.QApplication(sys.argv)

mw = MainWidget()
mw.show()

music = Bgm()
music.start()

exit(app.exec_())