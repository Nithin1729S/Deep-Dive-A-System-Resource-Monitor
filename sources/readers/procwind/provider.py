import time
from datetime import datetime

import psutil


def check_process_existence(prociden):
    try:
        psutil.Process(prociden)
        return True
    except psutil.NoSuchProcess:
        return False


def return_mainscreen_onetimed_statistics(prociden):
    procobjc = psutil.Process(prociden)
    retndata = {
        "prociden": procobjc.pid,
        "procname": procobjc.name(),
        "cpu_percent": procobjc.cpu_percent(),
        "memory_percent": procobjc.memory_percent(),
        "cpu_num": procobjc.cpu_num(),
        "num_threads": procobjc.num_threads(),
        "username": procobjc.username(),
        "terminal": procobjc.terminal(),
        "nice": procobjc.nice(),
        "ionice": procobjc.ionice().value,
        "num_ctx_switches": {
            "voluntary": procobjc.num_ctx_switches().voluntary,
            "involuntary": procobjc.num_ctx_switches().involuntary,
        },
        "ppid": procobjc.ppid(),
        "status": procobjc.status().title(),
        "create_time": datetime.fromtimestamp(procobjc.create_time()).strftime(
            "%Y-%m-%d, %H:%M:%S"
        ),
        "acquired_on": datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d, %H:%M:%S"),
    }
    return retndata
