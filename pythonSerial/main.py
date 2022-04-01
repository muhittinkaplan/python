from PyQt5.QtWidgets import QApplication,QDialog

import sys
import gui

from serialThreadFile import SerialThreadClass

class MainClass(QDialog,gui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClickedEvent)
        self.mySerial=SerialThreadClass()
        self.mySerial.mesaj.connect(self.textEdit.append)#elen verileri yazmak için kullanılan hat (pip)
        self.mySerial.start()#run thread

    def btnClickedEvent(self):
        self.mySerial.sendSerial('B')
        print("Pressing")

if __name__ == '__main__':
    uygulama=QApplication(sys.argv)
    pencere=MainClass()
    pencere.show()
    uygulama.exec_()