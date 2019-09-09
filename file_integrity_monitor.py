import os
import hashlib
import time

def fim():
    files = {}
    count = 1
    print("\n----------Performing integrity check----------")
    print("\nDate\t\tTime\t\tFile Updated")
    while count<=10:
        for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
            hash = hashlib.md5()
            with open(file) as f:
                for chunk in iter(lambda: f.read(1024), ""):
                    hash.update(chunk.encode('utf-8'))
                md5 = hash.hexdigest()
                if file in files and md5 != files[file]:
                    print('%s\t%s'%(time.strftime("%d-%m-%Y\t%H:%M:%S") , file))
                files[file] = md5
        time.sleep(5)
        count+=1
