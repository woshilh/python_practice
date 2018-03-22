#coding:utf-8
from multiprocessing import Pool
import os,time,random

def worker(msg):
    start = time.time()
    print("%s开始执行,进程号为%d" %(msg,os.getpid()))
    time.sleep(random.random()*2)
    stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(stop-start))

def main():
    po = Pool(3)
    for i in range(0,10):
        po.apply_async(worker,(i,))

    print("---start----")
    po.close()
    po.join()
    print("---end---")


if __name__ == "__main__":
    main()
