import os
import sys
import time

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def clear_screen():
    os.system("clear")

def display_banner():
    os.system("figlet Ha3MrX")

def main_menu():
    clear_screen()
    display_banner()
    print("Create By : Ha3MrX")
    print("           [1]> Brute Force              ")
    print("           [2]> DDos Attack              ")
    print("           [3]> NMap PortScanner         ")
    print("           [4]> Install Tools Hacking    ")
    print()
    print(" [0]> Exit ")
    print()

def get_user_choice():
    return input("Ha3MrX ==>> ")

def brute_force():
    os.system("python2 brute.py")

def ddos_attack():
    clear_screen()
    os.system("figlet DDOS Attack")
    ip = input("IP Address : ")
    port = input("Port       : ")
    packet = input("Packet     : ")
    os.system(f"python2 pntddos {ip} {port} {packet}")

def nmap_scan():
    clear_screen()
    os.system("figlet NMap Scan")
    host = input("Host : ")
    os.system(f"nmap {host}")

def install_tools_hacking():
    os.system("python2 lazymux.py")

def main():
    while True:
        main_menu()
        choice = get_user_choice()

        if choice in ["1", "01"]:
            brute_force()
        elif choice in ["2", "02"]:
            ddos_attack()
        elif choice in ["3", "03"]:
            nmap_scan()
        elif choice in ["4", "04"]:
            install_tools_hacking()
        elif choice in ["0", "00"]:
            sys.exit()
        else:
            print("\nERROR: Wrong Input")
            time.sleep(3)
            restart_program()

if __name__ == "__main__":
    main()
