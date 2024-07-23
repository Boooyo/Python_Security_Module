Python SYN Flood Attack Tool

You can start SYN Flood attack with this tool.

Simple and efficient.

## Dependencies
```
apt install python-scapy
apt install python3-scapy
```

## Installation

```
git clone https://github.com/EmreOvunc/Python-SYN-Flood-Attack-Tool.git
cd Python-SYN-Flood-Attack-Tool
```

## Usage

```
python3 py3_synflood_cmd.py -t 10.20.30.40 -p 8080 -c 5
python3 py3_SYN-Flood.py
python SYN-Flood.py
```
```
usage: py3_synflood_cmd.py [-h] [--target TARGET] [--port PORT]
                           [--count COUNT] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --target TARGET, -t TARGET
                        target IP address
  --port PORT, -p PORT  target port number
  --count COUNT, -c COUNT
                        number of packets
  --version, -v         show program's version number and exit

Usage: python3 py3_synflood_cmd.py -t 10.20.30.40 -p 8080 -c 1
```

![alt tag](https://emreovunc.com/projects/python_synflood_attack_cmd.png)

![alt tag](https://emreovunc.com/projects/Syn_Flood_01.png)

![alt tag](https://emreovunc.com/projects/Syn_Flood_02.png)

# Update(2024/07/23)
Add IPv6 support, you can use command like following
```
sudo python3 py3_synflood_cmd.py -t 2001:b030:7140:ac00:ed50:b959:3649:be45 -p 52916 -c 100 -f 6
```