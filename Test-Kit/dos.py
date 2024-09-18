import threading
import socket
import sys
import random
import time
import argparse

# ANSI colors for terminal output
F = '\033[91m'
E = '\033[0m'

# User agents list
user_agents = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"
]

# HTTP header template
http_headers = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
'''

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Stress test a web server.")
    parser.add_argument("target", help="Target website URL or IP")
    parser.add_argument("--threads", type=int, default=1000, help="Number of threads to use for the test")
    return parser.parse_args()

# Stress test function
def stress_test(target_site, user_agents):
    while True:
        try:
            # Create a new socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_site, 80))

            # Create HTTP request
            user_agent = random.choice(user_agents)
            request = f"GET / HTTP/1.1\nHost: {target_site}\nUser-Agent: {user_agent}\n{http_headers}".encode('utf-8')

            # Send HTTP request
            s.sendall(request)
            print(F + f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Sent request to {target_site} with User-Agent: {user_agent}" + E)

            # Close the socket
            s.close()
            time.sleep(random.uniform(0.1, 0.5))  # Add slight delay to prevent overwhelming the server
        except socket.error:
            print(F + f"Failed to connect to {target_site}. Exiting thread." + E)
            break

# Function to start the stress test
def start_stress_test(target_site, thread_count, user_agents):
    threads = []

    # Start the threads
    for _ in range(thread_count):
        thread = threading.Thread(target=stress_test, args=(target_site, user_agents))
        thread.daemon = True
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Keep the main thread alive to let other threads work
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(F + "\nTest interrupted. Exiting gracefully." + E)
        sys.exit(0)

if __name__ == "__main__":
    args = parse_arguments()
    start_stress_test(args.target, args.threads, user_agents)
