import sys

from readers.mainwind_mx import return_bottombar_onetimed_statistics
from screens.mainwind.mainwind_ui import Ui_mainwind
from screens.mainwind.mainwind_wk import Worker
from PyQt5 import QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *


class MainApp(QMainWindow, Ui_mainwind):
    def __init__(self):
        QMainWindow.__init__(self)
        self.title = "Resource Monitor"
        self.setupUi(self)
        self.setWindowTitle(self.title)
        self.obj = Worker()
        self.thread = QThread()
        self.prepare_bottombar_worker()
        self.handle_elements()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.thread.destroyed.connect(sys.exit())

    def prepare_bottombar_worker(self):
        self.obj.bottom_bar_ready.connect(self.on_bottombar_ready)
        self.obj.moveToThread(self.thread)
        self.thread.started.connect(self.obj.bottombar_statistics_emitter)
        self.thread.start()

    def handle_elements(self):
        retndata = return_bottombar_onetimed_statistics()
        self.userhost.setText("%s@%s" % (retndata["username"], retndata["hostname"]))
        self.kernvers.setText("%s %s" % (retndata["systname"], retndata["rlsename"]))

    def on_bottombar_ready(self, i):
        self.cpudperc.setText(str(i["cpud_percent"]))
        self.memoperc.setText(str(i["memo_percent"]))
        self.swapperc.setText(str(i["swap_percent"]))
        self.diskperc.setText(str(i["disk_percent"]))
