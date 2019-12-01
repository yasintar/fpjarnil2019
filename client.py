'''
    udp socket client
    Silver Moon
'''
from socket import *
   #for sockets
import sys  #for exit
 
# create dgram udp socket
try:
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
# host = 'localhost';
port = 8888;
 
while(1) :
    msg = raw_input('Enter message to send : ')
     
    try :
        #Set the whole string
        s.sendto(msg, ('255.255.255.255', port))
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print 'Server reply : ' + reply
     
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()