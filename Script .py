import os
os.system ('clear')
import socket
import system

print ("Enter Your DNS Target: ")
hostname = input()
ip=socket.gethostbyname(hostname)
print ("Host Name Is: ",hostname,"/n" "Target Ip Is: ",ip)
