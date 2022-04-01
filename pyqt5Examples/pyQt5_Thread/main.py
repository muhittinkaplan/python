from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
import sys
from gui.mainGui import  Ui_Dialog
import threadClassFile

class mywindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self,parent=None):
        super(mywindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.myThread=threadClassFile.ThreadClass()
        self.myThread.signal.connect(self.progressBarUpdate)
        self.myThread.start()

    @pyqtSlot(int)
    def progressBarUpdate(self,x):
        self.progressBar.setValue(x)
        if (x>20):
            QMessageBox.about(self,"MessageBoxCaption","MessageBoxText")

app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())