from PyQt5 import QtWidgets, uic
import sys
from firstGui import Ui_Dialog


class mywindow(QtWidgets.QMainWindow,Ui_Dialog):
    def __init__(self,parent=None):
        super(mywindow, self).__init__(parent=parent)

        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Buton Clicked")
        self.lineEdit.setText("Merhaba QT")
        self.label.setText("Yakarsa Dünyayı Garipler Yakar")
        self.label.setStyleSheet("background-color: lightgreen")
        self.setWindowTitle("Muhittin KAPLAN")


app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
