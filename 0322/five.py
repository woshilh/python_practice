#coding:utf-8

import threading

from time import sleep,ctime

def sing():
    for i in range(3):
        print("singing....%d" %i)
        sleep(1)

def dance():
    for i in range(3):
        print("danceing....%d" %i)
        sleep(1)


if __name__ == "__main__":
    print('----start----:%s'%ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('----stop----:%s'%ctime())


