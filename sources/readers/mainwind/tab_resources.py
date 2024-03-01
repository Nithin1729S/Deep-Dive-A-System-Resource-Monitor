import getpass
from os import uname

import psutil

from sources.readers import memory

mmrysize = memory()


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


def return_mainscreen_threaded_statistics():
    retndata = {
        "memo": {
            "percentage": {
                "used": psutil.virtual_memory().used * 100 / psutil.virtual_memory().total,
                "cached": psutil.virtual_memory().cached * 100 / psutil.virtual_memory().total,
                "free": psutil.virtual_memory().free * 100 / psutil.virtual_memory().total,
            },
            "absolute": {
                "used": mmrysize.format(psutil.virtual_memory().used),
                "cached": mmrysize.format(psutil.virtual_memory().cached),
                "free": mmrysize.format(psutil.virtual_memory().free),
                "total": mmrysize.format(psutil.virtual_memory().total),
                "active": mmrysize.format(psutil.virtual_memory().active),
                "buffers": mmrysize.format(psutil.virtual_memory().buffers),
                "shared": mmrysize.format(psutil.virtual_memory().shared),
                "slab": mmrysize.format(psutil.virtual_memory().slab),
            },
        },
        "swap": {
            "percentage": {
                "used": (psutil.swap_memory().used * 100 / psutil.swap_memory().total)
                if psutil.swap_memory().total > 0
                else 0,
                "free": (psutil.swap_memory().free * 100 / psutil.swap_memory().total)
                if psutil.swap_memory().total > 0
                else 100,
            },
            "absolute": {
                "used": mmrysize.format(psutil.swap_memory().used),
                "free": mmrysize.format(psutil.swap_memory().free),
                "total": mmrysize.format(psutil.swap_memory().total),
                "sin": mmrysize.format(psutil.swap_memory().sin),
                "sout": mmrysize.format(psutil.swap_memory().sout),
            },
        },
        "cpud": {
            "percentage": {
                "used": psutil.cpu_percent(),
                "free": 100 - psutil.cpu_percent(),
            },
            "absolute": {
                "ctx_switches": psutil.cpu_stats().ctx_switches,
                "interrupts": psutil.cpu_stats().interrupts,
                "soft_interrupts": psutil.cpu_stats().soft_interrupts,
                "sys_calls": psutil.cpu_stats().syscalls,
            },
        },
    }
    return retndata
