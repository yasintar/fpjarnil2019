from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

data = {"Ip-path-list": [], "Destination": "", "Message": ""}

while True:
    data["Message"] = raw_input()
    data["Destination"] = "192.168.0.1"
    s.sendto(str(data), ('255.255.255.255', 12345))
    
    m = s.recvfrom(1024)
    print m
