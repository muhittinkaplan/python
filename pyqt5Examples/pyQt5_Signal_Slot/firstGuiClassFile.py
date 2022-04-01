from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal,pyqtSlot
import secondGuiClassFile
import sys

class Ui(QtWidgets.QDialog):
    mySignal = pyqtSignal(str)#

    def __init__(self,parent=None):
        super(Ui, self).__init__(parent=parent)
        uic.loadUi('guiDir/firstGui.ui', self)
        self.formAcButton=self.findChild(QtWidgets.QPushButton,"pushButton")
        self.formAcButton.clicked.connect(self.digerFormAc)
        self.textGonderButton=self.findChild(QtWidgets.QPushButton,"pushButton_2")
        self.textGonderButton.clicked.connect(self.textGonder)
        self.textBox=self.findChild(QtWidgets.QLineEdit,"lineEdit")
        self.label=self.findChild(QtWidgets.QLabel,"label")
        self.show()

    def digerFormAc(self):
        self.digerForm=secondGuiClassFile.Ui(parent=self)#bu sınıfı diğer sınıfın parent i olarak belirliyoruz. birinci form kapatılırsa ikinci form da kapatılıyor.
        self.mySignal.connect(self.digerForm.changeText)
        self.digerForm.myIntSignal.connect(self.digerformdanGelenVeri)
        self.digerForm.labelBox.setText("Deneme")
        self.digerForm.show()

    def textGonder(self):
        self.mySignal.emit(self.textBox.text())

    @pyqtSlot(int)
    def digerformdanGelenVeri(self,x):
        self.label.setText(str(x))#Gelen veri int türünde, label de gösermek için Str ye çevirdik


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()