import serial
from PyQt5.QtCore import pyqtSignal,QThread

class SerialThreadClass(QThread):
    mesaj=pyqtSignal(str)

    def __init__(self,parent=None):
        super (SerialThreadClass,self).__init__(parent)
        self.seriport=serial.Serial()
        self.seriport.baudrate=9600
        self.seriport.port='/dev/ttyUSB0'#for linux FTDI
        self.seriport.open()

    def run(self):
        while True:
            veri=self.seriport.readline()
            self.mesaj.emit(str(veri))
            print(veri)

    def sendSerial(self,sendChar):
        self.seriport.write(b'A')#one byte
