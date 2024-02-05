import getpass
from os import uname

import psutil


def return_bottombar_threaded_statistics():
    retndata = {
        "cpud_percent": psutil.cpu_percent(),
        "memo_percent": psutil.virtual_memory().percent,
        "swap_percent": psutil.swap_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
    }
    return retndata


def return_bottombar_onetimed_statistics():
    retndata = {
        "username": getpass.getuser(),
        "hostname": uname().nodename,
        "systname": uname().sysname,
        "rlsename": uname().release,
    }
    return retndata
