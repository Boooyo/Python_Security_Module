import os
import sys
import subprocess
from time import sleep

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def clear_screen():
    subprocess.call('clear', shell=True)

def display_banner():
    clear_screen()
    subprocess.call('figlet Ha3MrX', shell=True)

def brute_force():
    subprocess.call('python2 brute.py', shell=True)

def ddos_attack():
    clear_screen()
    subprocess.call('figlet DDOS Attack', shell=True)
    ip = input("IP Address : ")
    port = input("Port       : ")
    packet = input("Packet     : ")
    subprocess.call(f'python2 pntddos {ip} {port} {packet}', shell=True)

def nmap_scan():
    clear_screen()
    subprocess.call('figlet NMap Scan', shell=True)
    host = input("Host : ")
    subprocess.call(f'nmap {host}', shell=True)

def install_tools():
    subprocess.call('python2 lazymux.py', shell=True)

def exit_program():
    sys.exit()

def main_menu():
    display_banner()
    print("Create By : Ha3MrX")
    print("           [1]> Brute Force              ")
    print("           [2]> DDos Attack              ")
    print("           [3]> NMap PortScanner         ")
    print("           [4]> Install Tools Hacking    ")
    print(" [0]> Exit ")
    print()
    
    menu_options = {
        "1": brute_force,
        "01": brute_force,
        "2": ddos_attack,
        "02": ddos_attack,
        "3": nmap_scan,
        "03": nmap_scan,
        "4": install_tools,
        "04": install_tools,
        "0": exit_program,
        "00": exit_program,
    }
    
    choice = input("Ha3MrX ==>> ")
    action = menu_options.get(choice, None)
    
    if action:
        action()
    else:
        print("\nERROR: Wrong Input")
        sleep(3)
        restart_program()

if __name__ == "__main__":
    main_menu()
