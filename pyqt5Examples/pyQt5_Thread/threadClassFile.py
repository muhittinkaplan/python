import time
from PyQt5.QtCore import QThread, pyqtSignal

class ThreadClass(QThread):
    signal = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)
        print("threadRun")
        self.i=0

    def run(self):
        while(self.i<25):
            self.signal.emit(self.i)
            self.i=self.i+1
            time.sleep(1)
