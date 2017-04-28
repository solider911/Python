#!/usr/bin/python
#Filename:using_pickle.py

# pickle存储方式默认是二进制方式
#import cPickle as p
import pickle as p

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot', '测试']

f=open(shoplistfile, 'wb')
p.dump(shoplist, f)
f.close()

del shoplist

f=open(shoplistfile, 'rb')
storedlist=p.load(f)
print(storedlist)
