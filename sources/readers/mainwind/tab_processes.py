import psutil

statistics_columns = [
    "pid",
    "name",
    "terminal",
    "username",
    "status",
    "cpu_percent",
    "memory_percent",
    "num_threads",
]


def return_processes_list():
    proclist, procqant = [], 0
    for proc in psutil.process_iter(statistics_columns):
        proclist.append(
            (
                str(proc.info["pid"]),
                str(proc.info["name"]),
                str(proc.info["terminal"]),
                str(proc.info["username"]),
                str(proc.info["status"]),
                "%2.1f" % proc.info["cpu_percent"],
                "%2.1f" % proc.info["memory_percent"],
                str(proc.info["num_threads"]),
            )
        )
        procqant += 1
    retndata = {"process_list": proclist, "process_count": procqant}
    return retndata
