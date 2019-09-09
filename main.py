import qualysapi
from qualysapi import connect
from lxml import objectify,etree
from file_integrity_monitor import *
import sys
from port_scanning import *

def get_number(call):
    xml = qualysConnection.request(call)
    xml = xml.encode('UTF-8')
    doc = etree.XML(xml)
    return doc.find('count').text

try:
    qualysConnection = qualysapi.connect('config.ini')  
    while(True):
        choice = int(input("1. File Integrity Monitoring 2. Scan Ports 3. Show number of webapps hosted 4. Show number of scans scheduled 5. Show number of reports generated 6. Show number of times scanned 7. Stop\nEnter choice: "))
        if choice==1:
            fim()
        elif choice==2:
            target_host = input("Enter the hostname to be scanned: ")
            scanPorts(target_host)
        elif choice==3:
            print("Number of webapps:",get_number('/count/was/webapp'),'\n')
        elif choice==4:
            print("Number of scan scheduled:",get_number('/count/was/wasscanschedule'),'\n')
        elif choice==5:
            print("Number of reports generated:",get_number('/count/was/report'),'\n')
        elif choice==6:
            print("Number of times scanned:",get_number('/count/was/wasscan'),'\n')
        elif choice==7:
            break
        else:
            print("Invalid choice. Enter again!")
except KeyboardInterrupt:
    sys.exit()
