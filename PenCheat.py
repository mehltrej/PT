import os
import socket
import nmap
import re
import sys
print sys.argv

strDomain = raw_input ('Input the domain: ')
dctCmdOut = {}

strPingResp = os.system("ping -c 1 " + intIpAddr)

#f strPingResp == 0:
#    for cmd in tplNmapScriptCmd:
#        strCommand = tplNmapScriptCmd[count]
#        print '\nCommand Running: ', cmd, '\n' #strCommand
#        dctCmdOut[count] = os.system(strCommand + " " + intIpAddr)
#        print dctCmdOut[count]
#        count = count + 1
os.system("cd ~")
os.system("mkdir OSINTout")
count = 0
while (count != 0):
    print '\n Command Running: whois \n'
    os.system("whois " + strDomain " > /home/OSINTout/output.txt")
    print '\n Command Running: dig DNS IP Lookup \n'
    os.system("dig a " + strDomain " > /home/OSINTout/output.txt")    
