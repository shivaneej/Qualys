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
    choice = int(input("1. Show number of webapps hosted\n2. Show number of scans scheduled\n3. Show number of reports generated\n4. Show number of times scanned:\n5. Stop\n"))
    if choice==1:
        print("Number of webapps:",get_number('/count/was/webapp'))
    elif choice==2:
        print("Number of scan scheduled:",get_number('/count/was/wasscanschedule'))
    elif choice==3:
        print("Number of reports generated:",get_number('/count/was/report'))
    elif choice==4:
        print("Number of times scanned:",get_number('/count/was/wasscan'))
    elif choice==5:
        break
    else:
        print("Invalid choice. Enter again!")
