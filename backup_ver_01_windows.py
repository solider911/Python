#!/usr/bin/python
#Filename:backup_ver_01.py

import os
import time
import zipfile

#source = [r'D:\cgit\python', r'D:\doc']
source = r'D:/cgit/python/test'

target_dir = r"D:/backup/"

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

f = zipfile.ZipFile( target, 'w', zipfile.ZIP_DEFLATED )  


# os.walk 方便很多了.这个方法返回的是一个三元tupple(dirpath, dirnames, filenames),
# 其中第一个为起始路径，
# 第二个为起始路径下的文件夹,
# 第三个是起始路径下的文件.
# dirpath是一个string，代表目录的路径,
# dirnames是一个list，包含了dirpath下所有子目录的名字,
# filenames是一个list，包含了非目录文件的名字.这些名字不包含路径信息,如果需要得到全路径,需要使用 os.path.join(dirpath, name)

for dirpath, dirnames, filenames in os.walk( source ):  
    print(dirpath)
    print(dirnames)
    print(filenames)
    for filename in filenames:
        print(filename)
        f.write(os.path.join(dirpath,filename))
f.close() 
