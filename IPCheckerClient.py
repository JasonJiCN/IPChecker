#coding=utf8
import os,sys,thread,threading,time
import thread

from urllib2 import urlopen

ipupdataUrl='http://127.0.0.1:7333/updata/' #ip 更新提交的地址

def getIP():
    my_ip = urlopen('http://ip.42.pl/raw').read()
    return my_ip

# 为线程定义一个函数
def print_time():
    currentip = ''
    while True:
        tempip=getIP()
        if tempip!=currentip:
            currentip=tempip
            urlopen(ipupdataUrl+currentip).read()

        time.sleep(10)


if __name__ == '__main__':
    threading.Thread(target=print_time).start()