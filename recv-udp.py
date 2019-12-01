from socket import *
import ast

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 12345))
while True:
    m = s.recvfrom(1024)
    sender_ip_address = m[1][0]
    data = ast.literal_eval(m[0])
    data["Ip-path-list"].append(sender_ip_address)
    print data
    a = "Pesan diterima"
    s.sendto(a, (sender_ip_address, 12345))
