#!/usr/bin/python
#Filename:bulletscreen.py
#coding:utf-8


from time import localtime
import socket
import time
#import urllib
#import urllib.request
import urllib2
import sqlite3
import os
import multiprocessing
import sys
import struct


host=socket.gethostbyname("openbarrage.douyutv.com")  #123.150.206.162
port=8601

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

import re
path=re.compile(b'txt@=(.+?)/cid@')
uid_path=re.compile(b'nn@=(.+?)/txt@')
level_path=re.compile(b'level@=([1-9][0-9]?)/egtt@')


def sendmsg(msgstr):
    #print('orgin msg:' + msgstr)
    msg = msgstr.encode('utf-8')
    #print('utf8_msg:%s' % msg) 
    data_length = len(msg) + 8
    code=689
    #msgHead = data_length.to_bytes(4, 'little') + data_length.to_bytes(4, 'little') + code.to_bytes(4, 'little')
    msgHead = struct.pack('iii', data_length, data_length, code)
    client.send(msgHead)
    sent=0
    while sent<len(msg):
        tn = client.send(msg[sent:])
        sent = sent+tn
    #print(client.recv(1024))

def get_name(roomid):
    url = "http://www.douyu.com/%d" % roomid
    #response = requests.get("http://www.douyu.com/" + roomid)
    response = urllib2.urlopen(url)
    print("response.status_code:%s" % response.getcode())
    print("response.headers:%s" % response.headers.getheader('content-type'))
    print(response.read())
    #soup = BeautifulSoup(r.text, 'lxml')
    #return soup.find('a', {'class', 'zb-name'}).string

def keeplive():
    while True:
        msg = 'type@keeplive/tick@=' +  str(int(time.time())) + '/\x00'
        print('keep_live_msg_send:%s' % msg)
        sendmsg(msg)
        print('keep_live_msg_recv:')
        print(client.recv(1024))
        time.sleep(40)

def start(roomid):           
     print('start coming...')
     msgLoginRequest='type@=loginreq/username@=/password@=/roomid@={}/\x00'.format(roomid)   # step1: login request
     sendmsg(msgLoginRequest)
     print("loginreq msg:")
     print(client.recv(1024))
     msgJoinGroupRequest='type@=joingroup/rid@={}/gid@=-9999/\x00'.format(roomid)  # step2: joingroup request
     sendmsg(msgJoinGroupRequest)
     #print(get_name(roomid))
     print("joingroup msg:")
     print(client.recv(1024))
     print('start looping...')
     
     while True:
            #print('start looping...')
	    data=client.recv(1024)
	    time.sleep(2)
	    continue;
	    #print(data)

	    data_more=path.findall(data)
	    uid_more=uid_path.findall(data)
	    level_more=level_path.findall(data)
	    if not data:
		continue
	    else:
                try:
                    for i in range(0,len(data_more)):
                        danmu = data_more[i]
                        danmu_decode = data_more[i].decode('utf-8')
                    
                        print(danmu_decode)
                        with open('bulletscreen.txt', 'a+') as f:
                            f.write(danmu+"\r\n")
                except:
                    print('danmu_decode exception!!!')
                    continue
                        
    
if __name__=='__main__':
    print('-- [pid]: %d main process starting --' % os.getpid())
    room_id=input("please enter the room_id:")
    p1=multiprocessing.Process(target=start,args=(room_id,))
    p1.start()
    
    time.sleep(3)
    p2=multiprocessing.Process(target=keeplive)
    p2.start()
    print("END!!!!!!!!!!!!!!!!!")

        

