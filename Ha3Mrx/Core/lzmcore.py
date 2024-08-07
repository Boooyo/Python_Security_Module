import os
import sys
import time

lazymux_banner = """
.-.                                           
: :                                           
: :    .--.  .---. .-..-.,-.,-.,-..-..-..-.,-.
: :__ ' .; ; `-'_.': :; :: ,. ,. :: :; :`.  .'
:___.'`.__,_;`.___;`._. ;:_;:_;:_;`.__.':_,._;
                    .-. :                     
                    `._.'                     
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the Lazymux
"""
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def backtomenu_option():
    print(backtomenu_banner)
    backtomenu = input("lzmx > ")
    
    if backtomenu == "99":
        restart_program()
    elif backtomenu == "00":
        sys.exit()
    else:
        print("\nERROR: Wrong Input")
        time.sleep(2)
        restart_program()

def banner():
    print(lazymux_banner)

def nmap():
    print('\n###### Installing Nmap')
    os.system('apt update && apt upgrade')
    os.system('apt install nmap')
    print('###### Done')
    print("###### Type 'nmap' to start.")
    backtomenu_option()

def red_hawk():
    print('\n###### Installing RED HAWK')
    os.system('apt update && apt upgrade')
    os.system('apt install git php')
    os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
    os.system('mv RED_HAWK ~')
    print('###### Done')
    backtomenu_option()

def dtect():
    print('\n###### Installing D-Tect')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/shawarkhanethicalhacker/D-TECT')
    os.system('mv D-TECT ~')
    print('###### Done')
    backtomenu_option()

def sqlmap():
    print('\n###### Installing sqlmap')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    os.system('mv sqlmap ~')
    print('###### Done')
    backtomenu_option()

def infoga():
    print('\n###### Installing Infoga')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('pip2 install requests urllib3 urlparse')
    os.system('git clone https://github.com/m4ll0k/Infoga')
    os.system('mv Infoga ~')
    print('###### Done')
    backtomenu_option()

def reconDog():
    print('\n###### Installing ReconDog')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/UltimateHackers/ReconDog')
    os.system('mv ReconDog ~')
    print('###### Done')
    backtomenu_option()

def androZenmap():
    print('\n###### Installing AndroZenmap')
    os.system('apt update && apt upgrade')
    os.system('apt install nmap curl')
    os.system('curl -O http://override.waper.co/files/androzenmap.txt')
    os.system('mkdir ~/AndroZenmap')
    os.system('mv androzenmap.txt ~/AndroZenmap/androzenmap.sh')
    print('###### Done')
    backtomenu_option()

def sqlmate():
    print('\n###### Installing sqlmate')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('pip2 install mechanize bs4 HTMLparser argparse requests urlparse2')
    os.system('git clone https://github.com/UltimateHackers/sqlmate')
    os.system('mv sqlmate ~')
    print('###### Done')
    backtomenu_option()

def astraNmap():
    print('\n###### Installing AstraNmap')
    os.system('apt update && apt upgrade')
    os.system('apt install git nmap')
    os.system('git clone https://github.com/Gameye98/AstraNmap')
    os.system('mv AstraNmap ~')
    print('###### Done')
    backtomenu_option()

def wtf():
    print('\n###### Installing WTF')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('pip2 install bs4 requests HTMLParser urlparse mechanize argparse')
    os.system('git clone https://github.com/Xi4u7/wtf')
    os.system('mv wtf ~')
    print('###### Done')
    backtomenu_option()

def easyMap():
    print('\n###### Installing Easymap')
    os.system('apt update && apt upgrade')
    os.system('apt install php git')
    os.system('git clone https://github.com/Cvar1984/Easymap')
    os.system('mv Easymap ~')
    os.system('cd ~/Easymap && sh install.sh')
    print('###### Done')
    backtomenu_option()

def xd3v():
    print('\n###### Installing XD3v')
    os.system('apt update && apt upgrade')
    os.system('apt install curl')
    os.system('curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
    os.system('mv xd3v.sh ~/../usr/bin/xd3v && chmod +x ~/../usr/bin/xd3v')
    print('###### Done')
    print("###### Type 'xd3v' to start.")
    backtomenu_option()

def crips():
    print('\n###### Installing Crips')
    os.system("apt update && apt upgrade")
    os.system("apt install git python2 openssl curl libcurl wget")
    os.system("git clone https://github.com/Manisso/Crips")
    os.system("mv Crips ~")
    print('###### Done')
    backtomenu_option()

def sir():
    print('\n###### Installing SIR')
    os.system("apt update && apt upgrade")
    os.system("apt install python2 git")
    os.system("pip2 install bs4 urllib2")
    os.system("git clone https://github.com/AeonDave/sir.git")
    os.system("mv sir ~")
    print('###### Done')
    backtomenu_option()

def xshell():
    print('\n###### Installing Xshell')
    os.system("apt update && apt upgrade")
    os.system("apt install lynx python2 figlet ruby php nano w3m")
    os.system("git clone https://github.com/Ubaii/Xshell")
    os.system("mv Xshell ~")
    print('###### Done')
    backtomenu_option()

def evilURL():
    print('\n###### Installing EvilURL')
    os.system("apt update && apt upgrade")
    os.system("apt install git python2 python3")
    os.system("git clone https://github.com/UndeadSec/EvilURL")
    os.system("mv EvilURL ~")
    print('###### Done')
    backtomenu_option()

def striker():
    print('\n###### Installing Striker')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('git clone https://github.com/UltimateHackers/Striker')
    os.system('mv Striker ~')
    os.system('cd ~/Striker && pip2 install -r requirements.txt')
    print('###### Done')
    backtomenu_option()

def dsss():
    print('\n###### Installing DSSS')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/stamparm/DSSS')
    os.system('mv DSSS ~')
    print('###### Done')
    backtomenu_option()

def sqliv():
    print('\n###### Installing SQLiv')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/Hadesy2k/sqliv')
    os.system('mv sqliv ~')
    print('###### Done')
    backtomenu_option()

def sqlscan():
    print('\n###### Installing sqlscan')
    os.system('apt update && apt upgrade')
    os.system('apt install git php')
    os.system('git clone http://www.github.com/Cvar1984/sqlscan')
    os.system('mv sqlscan ~')
    print('###### Done')
    backtomenu_option()

def wordpreSScan():
    print('\n###### Installing Wordpresscan')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
    os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
    os.system('mv Wordpresscan ~')
    print('###### Done')
    backtomenu_option()

def fscan():
    print('\n###### Installing Fscan')
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/shadow1n/fscan')
    os.system('mv fscan ~')
    print('###### Done')
    backtomenu_option()

def hacktools():
    print('\n###### Installing HackTools')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('git clone https://github.com/Ha3MrX/HackTools')
    os.system('mv HackTools ~')
    print('###### Done')
    backtomenu_option()

def xsscrapy():
    print('\n###### Installing XSSCrappy')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('git clone https://github.com/epinna/XSSCrappy')
    os.system('mv XSSCrappy ~')
    print('###### Done')
    backtomenu_option()

def termux_tool():
    print('\n###### Installing Termux Tool')
    os.system('apt update && apt upgrade')
    os.system('apt install git')
    os.system('git clone https://github.com/adiwajshing/Bdsm-Termux')
    os.system('mv Bdsm-Termux ~')
    print('###### Done')
    backtomenu_option()

def iscan():
    print('\n###### Installing iScan')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/MrUn1k0d3r/iScan')
    os.system('mv iScan ~')
    print('###### Done')
    backtomenu_option()

def xsspy():
    print('\n###### Installing XSSPY')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('git clone https://github.com/0x1n/XSsPY')
    os.system('mv XSsPY ~')
    print('###### Done')
    backtomenu_option()

def cspy():
    print('\n###### Installing CSPY')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/s0md3v/CSPY')
    os.system('mv CSPY ~')
    print('###### Done')
    backtomenu_option()

def portscan():
    print('\n###### Installing PortScan')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/t00ls/PortScan')
    os.system('mv PortScan ~')
    print('###### Done')
    backtomenu_option()

def bigxss():
    print('\n###### Installing BigXSS')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('git clone https://github.com/0x4D3v/BigXSS')
    os.system('mv BigXSS ~')
    print('###### Done')
    backtomenu_option()

def backdoor():
    print('\n###### Installing Backdoor')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/h00die/Backdoor')
    os.system('mv Backdoor ~')
    print('###### Done')
    backtomenu_option()

def webshell():
    print('\n###### Installing WebShell')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('git clone https://github.com/0x4D3v/WebShell')
    os.system('mv WebShell ~')
    print('###### Done')
    backtomenu_option()

def crack():
    print('\n###### Installing Crack')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/looxxi/Crack')
    os.system('mv Crack ~')
    print('###### Done')
    backtomenu_option()

def d2f():
    print('\n###### Installing D2F')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/d2f/d2f')
    os.system('mv d2f ~')
    print('###### Done')
    backtomenu_option()

def exploit():
    print('\n###### Installing Exploit')
    os.system('apt update && apt upgrade')
    os.system('apt install git python2')
    os.system('git clone https://github.com/g0rx/Exploit')
    os.system('mv Exploit ~')
    print('###### Done')
    backtomenu_option()

def ninja():
    print('\n###### Installing Ninja')
    os.system('apt update && apt upgrade')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/0x0ninja/Ninja')
    os.system('mv Ninja ~')
    print('###### Done')
    backtomenu_option()
