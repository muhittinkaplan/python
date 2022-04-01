from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtCore import pyqtSignal, pyqtSlot

class Ui(QtWidgets.QDialog):
    myIntSignal = pyqtSignal(int)  #

    def __init__(self,parent=None):
        super(Ui, self).__init__(parent=parent)
        uic.loadUi('guiDir/secondGui.ui', self)
        self.labelBox = self.findChild(QtWidgets.QLabel, "label")#ui içerisindeki label bulunuyor
        self.button=self.findChild(QtWidgets.QPushButton, "pushButton")
        self.button.clicked.connect(self.form1VeriDegistir)
        self.textBox=self.findChild(QtWidgets.QLineEdit,"lineEdit")
        self.show()

    def form1VeriDegistir(self):
        self.myIntSignal.emit(int(self.textBox.text()))#signal  int türünde göndereceğimizi belittiğimizden int e çevirdik
    @pyqtSlot(str)
    def changeText(self,x):
        self.labelBox.setText(x)

