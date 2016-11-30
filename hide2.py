#!/usr/bin/python
# ---------------
# Once again, personal script
# incase that "situation" has
# comeforth.
# ---------------

# Updated script from a new base. Old one wasn't great. This one is more simple.
# created by devopia.
# Works!

import os
import re
import subprocess
import sys
import shutil
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m [*] '
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def emergency_mode_quiet():
	print  "                 ----o--              "
	print  " _____________   %%% , ,%_________    "
	print  "(___________,,)  %c    >) ,________)  "
	print  "   (_________,,)  )   =  ,______)     "
	print  "        (_____,,)/ _/__,,____)        "
	print  "           / \   \__/ /\              "
	print  "          /\ |        \/\             "
	print  "         /__\|'   ,   /  \,           "
	print  "        < -  '====o==,  /_\           "
	print  "       /    /`       |\ __ \          "
	print  "      /__,_/    |  _/, \____\         "
	print  "      //   |     \/  \    \\          "
	print  "    _( \   \      \  \   _/ \         "
	print  "     //|    \     \  \    |/|         "
	print  "            < `  _\ -)                "
	print  "           /    |_/ |                 "
	print  "          |    / |_/                  "
	print  "         /-_,  ' /|   
	print  "         \/ \_,--.,                   "
	print  "         '(    )'                     "
	print  "        / |    | \     dude, come on. "
	print  "        |,/    \,/                    "
	print  "                   		      "
	os.system("find /root -type f -iname \*.doc -delete")
	os.system("find /root -type f -iname \*.xlsx -delete")
	os.system("find /root -type f -iname \*.ppt -delete")
	os.system("find /root -type f -iname \*.html -delete")
	os.system("find /root -type f -iname \*.jpeg -delete")
	os.system("find /root/Desktop -type -f iname \*.jpeg -delete")
	os.system("find /root -type f -iname \*.apk -delete")
	os.system("find /root -type f -iname \*.apk -delete")
	os.system("find /var/lib/veil-evasion -type f -iname \*.exe -delete")
	os.system("find /var/lib/veil-evasion -type f -iname \*.txt -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.py -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.rb -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.c -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.cs -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.bat -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.go -delete")
	os.system("find /root/.msf4 -type -iname \*.log -delete")
	os.system("find /root/.msf4/logs -iname \*.log -delete")
	os.system("rm -r .msf4/logs/persistence")
	os.system("mkdir .msf4/logs/persistence")
	os.system("tput reset")
	print bcolors.BOLD + bcolors.OKGREEN + "done. Cleaning up now." + bcolors.ENDC	
	time.sleep(2)	
	os.system("clear")
	os.system("exit")


def print_menu():
	print 30 * " "	
	print "------------------------------"
	print " _     _     _        _ _     "
	print "| |   (_)   | |      (_) |    "
	print "| |__  _  __| | ___   _| |_   "
	print "| '_ \| |/ _\` |/ _ \ | | __| "
	print "| | | | | (_| |  __/ | | |_ _ "
	print "|_| |_|_|\__,_|\___| |_|\__(_)"
	print "                              "
	print "------------------------------"
	print 30 * "-" , "Main menu" , 30 * "-"
	print 30 * " "
	print "1. Remove pictures/screenshots"
	print "2. Remove Documents"
	print bcolors.BOLD + bcolors.WARNING + "3. Emergency Mode! (WIPE ALL!)" + bcolors.ENDC
	print bcolors.BOLD + bcolors.FAIL + "4. Emergency Mode! (Quiet)" + bcolors.ENDC
	print "5. Move all stuff to encrypted hidden folder."
	print "6. Remove all Malware. (APKS, EXE, Veil-Evasion)" 	
	print "7. Clear Metasploit/Meterpreter logs."	
	print 30 * " "
	print 60 * "-"

os.system("clear")
print_menu()
 
## Get input ###
choice = raw_input('Enter your choice [1-7] : ')
 
### Convert string to int type ##
choice = int(choice)
 
### Take action as per selected menu-option ###
if choice == 1:
	print bcolors.BOLD + bcolors.WARNING + "Wiping all screenshots and pictures from folders." + bcolors.ENDC        
	os.system("find /root -type f -iname \*.jpeg -delete")
	os.system("find /root/Desktop -type -f iname \*.jpeg -delete")
	print bcolors.BOLD + bcolors.OKGREEN + "done!"
	os.system("tput reset")
	time.sleep(1)
	print_menu()

elif choice == 2:
	os.system("clear")
	print bcolors.BOLD + bcolors.WARNING + "Wiping all documents from folders.." + bcolors.ENDC        
	os.system("find /root -type f -iname \*.doc -delete")
	os.system("find /root -type f -iname \*.xlsx -delete")
	os.system("find /root -type f -iname \*.ppt -delete")
	os.system("find /root -type f -iname \*.html -delete")
	print bcolors.BOLD + bcolors.OKGREEN + "done!" + bcolors.ENDC
	os.system("tput reset")	
	time.sleep(2)
	print_menu()

elif choice == 3:
        os.system("clear")
	print bcolors.BOLD + bcolors.FAIL + "emergency mode activiated. Wiping everything." + bcolors.ENDC
	print bcolors.BOLD + bcolors.WARNING + "Wiping Documents.." + bcolors.ENDC	
	os.system("find /root -type f -iname \*.doc -delete")
	os.system("find /root -type f -iname \*.xlsx -delete")
	os.system("find /root -type f -iname \*.ppt -delete")
	os.system("find /root -type f -iname \*.html -delete")
	time.sleep(1)	
	print bcolors.BOLD + bcolors.WARNING + "Wiping Pictures and Screenshots..." + bcolors.ENDC			
	time.sleep(1)	
	os.system("find /root -type f -iname \*.jpeg -delete")
	print bcolors.BOLD + bcolors.WARNING + "Wiping malware..." + bcolors.ENDC
	time.sleep(1)	
	os.system("find /root -type f -iname \*.apk -delete")
	os.system("find /var/lib/veil-evasion -type f -iname \*.exe -delete")
	os.system("find /var/lib/veil-evasion -type f -iname \*.txt -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.py -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.rb -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.c -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.cs -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.bat -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.go -delete")		
	os.system("tput reset")
	os.system("clear")
	print "done."
	print_menu()


elif choice == 4:
	os.system("clear")
	emergency_mode_quiet()

elif choice == 5:
	os.system("clear")
	os.system("mkdir /root/ssd32dl")
	os.system("mv *.xlsx /root/ssd32dl")
	os.system("mv *.doc /root/ssd32dl")
	os.system("mv *.jpeg /root/ssd32dl")
	os.system("mv *.mp3 /root/ssd32dl")
	os.system("zip --password ##ka##li## bashsystem.zip ssd32dl")
	os.system("rmdir /root/ssd32dl")
	os.system("mv bashsystem.zip /var/")
	os.system("clear")
	os.system("tput reset")	
	print "finished. You know the password."
	time.sleep(3)
	os.system("exit")	
	

elif choice == 6:
	os.system("clear")
	print bcolors.BOLD + bcolors.WARNING + "Wiping the malware!" + bcolors.ENDC	
	os.system("find /root -type f -iname \*.apk -delete")
	os.system("find /var/lib/veil-evasion -type f -iname \*.exe -delete")
	os.system("find /var/lib/veil-evasion -type f -iname \*.txt -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.py -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.rb -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.c -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.cs -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.bat -delete")
	os.system("find /var/lib/veil-evasion/output/source -type f -iname \*.go -delete")
	os.system("tput reset")
	print bcolors.BOLD + bcolors.OKGREEN + "done!"
	os.system("clear")
	os.system("exit")


elif choice == 7:
	print bcolors.BOLD + bcolors.OKBLUE + "Removing all logs, persistence settings from the msf4 folder." + bcolors.ENDC
	os.system("find /root/.msf4 -type -iname \*.log -delete")
	os.system("find /root/.msf4/logs -iname \*.log -delete")
	os.system("rm -r .msf4/logs/persistence")
	os.system("mkdir .msf4/logs/persistence")
	os.system("rm .msf4/history")
	os.system("exit")

else:    ## Message if you don't choose something from the menu. ##
        print ("Come on. Choose something from the menu.")
	time.sleep(1)	
	os.system("python hide2.py")
