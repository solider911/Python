#!/usr/bin/python
#Filename:backup_ver_01.py

import os
import time

#source = [r'D:\cgit\python', r'D:\doc']
source = r'D:/cgit/python/test'

target_dir = r"D:/backup/"

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

print(target)

zip_command = "zip %s %s " % (target, source)

print(zip_command)

if os.system(zip_command) == 0:
    print('successful backup to', target)
else:
    print('backup failed!')
