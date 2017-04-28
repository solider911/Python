#!/usr/bin/python
#Filename:try_except.py



# pickle存储方式默认是二进制方式
#import cPickle as p
import pickle as p
import sys
import os


#shoplistfile = 'shoplists.data'
shoplistfile = 'shoplist.data'
#shoplist = ['apple', 'mango', 'carrot', '测试']
#f=open(shoplistfile, 'wb')
#p.dump(shoplist, f)
#f.close()
#del shoplist


class FileException(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg=msg


try:
    if os.path.exists(shoplistfile) == 0:
       raise FileException('file not exists!')
    
    f=open(shoplistfile, 'rb')
    if f==0:
        raise FileException('file open failed!')
    
    storedlist=p.load(f)
    print(storedlist)
    f.close();

except FileException as fe:
    print(fe.msg)
    sys.exit()
except:
    print("open %s successed!" % shoplistfile)
     

print('read over!')
