import time

from readers.mainwind_mx import return_bottombar_threaded_statistics
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class Worker(QObject):
    finished = pyqtSignal()
    bottom_bar_ready = pyqtSignal(dict)

    @pyqtSlot()
    def bottombar_statistics_emitter(self):
        while True:
            time.sleep(1)
            a = return_bottombar_threaded_statistics()
            print(a)
            self.bottom_bar_ready.emit(a)
