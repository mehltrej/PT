#Enumeration & Attacking Network Services

import os
import subprocess
import socket
#import nmap
import re
import sys
print sys.argv

intIPAddr = raw_input ('Input the IP Address: ')
intIPSub = raw_input ('Input the IP Address Space: ')
print 'Input Taken'

if not os.path.exists("/home/OSINTout"):
    os.makedirs("/home/OSINTout")

count = 1
while (count != 0):
    print '\n Command Running: NMAP \n'
    with open('/home/OSINTout/netEnumAttackOut.txt', "w") as myfile:
        myfile.write("\n\t\t ********* SMB Enumeration *********** \n")

    #os.system("nmblookup -A " + intIPAddr + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("enum4linux -a " + intIPAddr + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("python /usr/share/doc/python-impacket/examples/samrdump.py " + intIPAddr + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("rlogin -l root " + intIPAddr + " >> /home/OSINTout/netEnumAttackOut.txt")
    print '\n Command Running: NBTSCAN \n'
    with open('/home/OSINTout/netEnumAttackOut.txt', "a") as myfile:
        myfile.write("\n\t\t ********* NBTScan *********** \n")
    #os.system("nbtscan " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("nbtscan -V" + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("nbtscan -f" + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")

    print '\n Command Running: NBTSCAN UNIXWIZ \n'
    with open('/home/OSINTout/netEnumAttackOut.txt', "a") as myfile:
        myfile.write("\n\t\t ********* NBTScan Unixwiz *********** \n")

    os.system("nbtscan-unixwiz -f " + intIPAddr + " >> /home/OSINTout/netEnumAttackOut.txt")


    with open('/home/OSINTout/netEnumAttackOut.txt', "a") as myfile:
        myfile.write("\n\t\t ********* SNMP Enumeration *********** \n")

    #os.system("nmap -sV -p 161 --script=snmp-info " + intIPSub + "/home/OSINTout/netEnumAttackOut.txt")
    #os.system("nmap -sU -sS --script=smb-enum-users -p U:137,T:139 " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")
    
    with open('/home/OSINTout/netEnumAttackOut.txt', "a") as myfile:
        myfile.write("\n\t\t ********* Oracle Database Testing *********** \n")

    #os.system("oscanner -s " + intIPSub + " -P 1521" + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("tnscmd10g version -h " + intIPAddr + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("nmap --script=oracle-tns-version " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("nmap --script=oracle-sid-brute " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("nmap --script=oracle-sid-brute " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("nmap -p 1521 -A " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")

    with open('/home/OSINTout/netEnumAttackOut.txt', "a") as myfile:
        myfile.write("\n\t\t ********* MSSQL *********** \n")

    #os.system("nmap -sU --script=ms-sql-info " + intIPAddr + " >> /home/OSINTout/netEnumAttackOut.txt")

    with open('/home/OSINTout/netEnumAttackOut.txt', "a") as myfile:
    	myfile.write("\n\t\t ********* IKEForce VPN Enumeration *********** \n")

    #os.system("ike-scan " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("ike-scan -A " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")

    with open('/home/OSINTout/netEnumAttackOut.txt', "a") as myfile:
    	myfile.write("\n\t\t ********* PPTP Hacking *********** \n")

    #os.system("nmap -Pn -sV -p 1723 " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")

    with open('/home/OSINTout/netEnumAttackOut.txt', "a") as myfile:
   		myfile.write("\n\t\t ********* HTTP/HTTPS Webserver Enumeration *********** \n")

    #os.system("nikto -h " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")

    with open('/home/OSINTout/netEnumAttackOut.txt', "a") as myfile:
    	myfile.write("\n\t\t ********* SMB & SNMP User Enumeration *********** \n")

    #os.system("python /usr/share/doc/python-impacket/examples/samrdump.py " + intIPAddr + " >> /home/OSINTout/netEnumAttackOut.txt")
    #os.system("nmap -sT -p " + intIPSub + " >> /home/OSINTout/netEnumAttackOut.txt")
    count = 0



