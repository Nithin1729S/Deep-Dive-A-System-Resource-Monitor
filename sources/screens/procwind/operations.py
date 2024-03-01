import time
from datetime import datetime

from PyQt5.QtWidgets import QDialog

from sources.readers.procwind.controller import (
    kill_process,
    resume_process,
    suspend_process,
    terminate_process,
)
from sources.readers.procwind.provider import return_mainscreen_onetimed_statistics
from sources.screens.procwind.interface import Ui_procwind


class ProcWind(QDialog, Ui_procwind):
    def __init__(self, prociden, sttusbar, parent=None):
        super(ProcWind, self).__init__(parent)
        self.title = "PID #%s" % (prociden)
        self.prociden = int(prociden)
        self.sttusbar = sttusbar
        self.setupUi(self)
        self.setWindowTitle(self.title)
        self.initialize_mainscreen_contents()

    def perform_process_killing(self):
        self.sttusbar.showMessage(
            "[%s] %s"
            % (
                datetime.fromtimestamp(time.time()).strftime("%H:%M:%S"),
                kill_process(self.prociden),
            )
        )
        self.hide()

    def perform_process_termination(self):
        self.sttusbar.showMessage(
            "[%s] %s"
            % (
                datetime.fromtimestamp(time.time()).strftime("%H:%M:%S"),
                terminate_process(self.prociden),
            )
        )
        self.hide()

    def perform_process_resuming(self):
        self.sttusbar.showMessage(
            "[%s] %s"
            % (
                datetime.fromtimestamp(time.time()).strftime("%H:%M:%S"),
                resume_process(self.prociden),
            )
        )
        self.hide()

    def perform_process_suspension(self):
        self.sttusbar.showMessage(
            "[%s] %s"
            % (
                datetime.fromtimestamp(time.time()).strftime("%H:%M:%S"),
                suspend_process(self.prociden),
            )
        )
        self.hide()

    def initialize_mainscreen_contents(self):
        retndata = return_mainscreen_onetimed_statistics(self.prociden)
        self.procname.setText(retndata["procname"])
        self.pcidtext.setText("#%d" % retndata["prociden"])
        self.cpudtext.setText("%2.1f%%" % retndata["cpu_percent"])
        self.memotext.setText("%2.1f%%" % retndata["memory_percent"])
        self.procccnm.setText(str(retndata["cpu_num"]))
        self.proctcnm.setText(str(retndata["num_threads"]))
        self.proccbnm.setText(str(retndata["username"]))
        self.proctmnm.setText(str(retndata["terminal"]))
        self.procepnm.setText(str(retndata["nice"]))
        self.procipnm.setText(str(retndata["ionice"]))
        self.procvcnm.setText(str(retndata["num_ctx_switches"]["voluntary"]))
        self.procicnm.setText(str(retndata["num_ctx_switches"]["voluntary"]))
        self.procppnm.setText(str(retndata["ppid"]))
        self.procsenm.setText(str(retndata["status"]))
        self.procstnm.setText(str(retndata["create_time"]))
        self.procmtrc.setText("Metrics acquired on %s." % str(retndata["acquired_on"]))
        self.procklbt.clicked.connect(self.perform_process_killing)
        self.proctmbt.clicked.connect(self.perform_process_termination)
        self.procrsbt.clicked.connect(self.perform_process_resuming)
        self.procspbt.clicked.connect(self.perform_process_suspension)
