#Port Scanning
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
    with open('/home/OSINTout/portScanOut.txt', "w") as myfile:
        myfile.write("\n\t\t ********* NMAP *********** \n")

    os.system("nmap -V -sS -A -T4 " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -sC -p22,111,139 -T4 " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -sP --script discovery " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -PN " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -PA " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -PU " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -PO " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -PR " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -r " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -PP -Pn " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -v -sU -sS -p- -A -T4 " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")
    os.system("nmap -sU " + intIPAddr + " >> /home/OSINTout/portScanOut.txt")

    print '\n Command Running: fping \n'
    with open('/home/OSINTout/portScanOut.txt', "a") as myfile:
        myfile.write("\n\t\t ********* fping *********** \n")

    os.system("fping -a -r 0 -g " + intIPSub + " >> /home/OSINTout/portScanOut.txt")


    count = 0
