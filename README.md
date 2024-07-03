# Deep Dive: A System Resource Monitor

A System resource monitoring tool leveraging Python libraries like Psutil, os, PyCPUInfo, Disto and Qt GUI interface for comprehensive real-time tracking and analysis of system resources

More details can be found in the [report](https://drive.google.com/file/d/1GqvxKrw88ipwJb8nq0WJaX_sKlFkD2sM/view?usp=sharing).

## Demo of the Project 



https://github.com/Nithin1729S/Deep-Dive-A-System-Resource-Monitor/assets/78496667/81d02633-7ec8-46b3-8412-9b46bdde2411


## Screenshots
![Screenshot from 2024-03-04 22-32-57](https://github.com/Nithin1729S/Deep-Dive-A-System-Resource-Monitor/assets/78496667/36769311-ba4d-41da-a0bf-42b27b74d18d)


![Screenshot from 2024-03-04 22-33-00](https://github.com/Nithin1729S/Deep-Dive-A-System-Resource-Monitor/assets/78496667/855e0591-f16c-41a2-ad09-57c937a561ba)

![Screenshot from 2024-03-04 22-33-02](https://github.com/Nithin1729S/Deep-Dive-A-System-Resource-Monitor/assets/78496667/e7b18ef8-aa2a-44da-9089-4e1e8a06d6e3)
![Screenshot from 2024-03-04 22-33-03](https://github.com/Nithin1729S/Deep-Dive-A-System-Resource-Monitor/assets/78496667/db36fcf2-d8eb-4dc7-9550-32c057b71cd3)

![Screenshot from 2024-03-04 22-33-04](https://github.com/Nithin1729S/Deep-Dive-A-System-Resource-Monitor/assets/78496667/ba5f63ba-edcd-447c-9dd4-c0b1bbe3cff6)
![Screenshot from 2024-03-04 22-33-05](https://github.com/Nithin1729S/Deep-Dive-A-System-Resource-Monitor/assets/78496667/e2312fc9-bcb3-49f8-bb3c-f4775f6f3ed6)



## Features

- **CPU**: Percentage, Clock Speeds, Occupancy, Duration, Counts of Context Switches, System calls and hardware interrupts
- **Memory**: Utilization, Swapping rate, Occupancy, Physical and logical partition
- **Internet**: Packet Count, Size, Rate, Transfer rate, Transmission, Dropped transfers
- **Processes**: PIDs, names, terminal, usernames, states, CPU/Memory Usage, context switches, threads, Kill, resume, Terminate, Suspend Options
- **System/Hardware**: OS, Kernel names, Versions, CPU name, Vendor, Frequency, Features

- Visually represent real-time data changes for clear understanding


## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Create a virtual environment:
    ```bash
    virtualenv env
    ```

3. Activate the virtual environment:
    ```bash
    source env/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the main script:
    ```bash
    python main.py
