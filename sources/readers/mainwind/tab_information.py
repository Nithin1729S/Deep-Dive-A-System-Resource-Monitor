from datetime import datetime
from os import uname
from sys import version as pythvers
import distro
import psutil
from cpuinfo import CPUINFO_VERSION_STRING as cpuivers
from distro import __version__ as distvers
from psutil import __version__ as psutvers
from PyQt5.QtCore import qVersion as pyqtvers

def return_software_information():
    retndata = {
        "name": distro.name(),
        "version": distro.version(),
        "hostname": uname().nodename,
        "release": uname().release,
        "rendition": uname().version,
        "boottime": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d, %H:%M:%S"),
    }
    return retndata


def return_obserware_information():
    retndata = {
        "pythvers": pythvers,
        "pyqtvers": pyqtvers(),
        "psutvers": psutvers,
        "cpuivers": cpuivers,
        "distvers": distvers,
    }
    return retndata


def is_distributed_via_flatpak():
    return distro.name() == "KDE Flatpak runtime"
