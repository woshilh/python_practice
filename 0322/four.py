#coding:utf-8

from multiprocessing import Process,Queue

q = Queue(3)
q.put("msg1")
q.put("msg2")
print(q.full())
q.put("msg3")
print(q.full())

try:
    q.put("msg4",True,2)
except:
    print("消息队列已满，现有消息数量：%s" %q.qsize())


if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
