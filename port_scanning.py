from socket import *


def scanPorts(target_host):
    target_IP = gethostbyname(target_host)
    print ('Scanning host: ',target_IP)
    for i in range(1, 1025):
        sock = socket(AF_INET, SOCK_STREAM)
        conn = sock.connect_ex((target_IP, i))
        if(conn == 0) :
            print ('Port %d: OPEN' % (i,))
        sock.close()