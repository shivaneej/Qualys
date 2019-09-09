import qualysapi
from qualysapi import connect
from lxml import objectify,etree

def get_number(call):
    xml = qualysConnection.request(call)
    xml = xml.encode('UTF-8')
    doc = etree.XML(xml)
    return doc.find('count').text

qualysConnection = qualysapi.connect('config.ini')  
while(True):
    choice = int(input("1. Show number of webapps hosted 2. Show number of scans scheduled 3. Show number of reports generated 4. Show number of times scanned 5. Stop\nEnter choice: "))
    if choice==1:
        print("Number of webapps:",get_number('/count/was/webapp'),'\n')
    elif choice==2:
        print("Number of scan scheduled:",get_number('/count/was/wasscanschedule'),'\n')
    elif choice==3:
        print("Number of reports generated:",get_number('/count/was/report'),'\n')
    elif choice==4:
        print("Number of times scanned:",get_number('/count/was/wasscan'),'\n')
    elif choice==5:
        break
    else:
        print("Invalid choice. Enter again!")
