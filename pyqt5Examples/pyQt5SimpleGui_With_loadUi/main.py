from PyQt5 import QtWidgets, uic
import sys

from numba.cuda import selp


class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('guiDir/firstGui.ui', self)
        self.button=self.findChild(QtWidgets.QPushButton,"pushButton")
        self.button.clicked.connect(self.buttonClicked)
        self.lineEdit=self.findChild(QtWidgets.QLineEdit,"lineEdit")
        self.label=self.findChild(QtWidgets.QLabel,"label")

        self.show()

    def buttonClicked(self):
        print("Buton Clicked")
        self.lineEdit.setText("Merhaba QT")
        self.label.setText("Yakarsa Dünyayı Garipler Yakar")
        self.label.setStyleSheet("background-color: lightgreen")
        self.setWindowTitle("Muhittin KAPLAN")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
