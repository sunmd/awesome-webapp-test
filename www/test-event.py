 # -*- coding: utf-8 -*-
#! /usr/bin/env python3
"""
Spyder Editor

This is a temporary script file.
"""

import time
import threading

class my_thread_event(threading.Thread):
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event

    def run(self):
        print("Thread : {} start at {}".format(self.name, time.ctime(time.time())))

        # 等待event.set 之后在执行
        self.event.wait()
        print("Thread : {} finish at {}".format(self.name, time.ctime(time.time())))
        
threads = []
event = threading.Event()

# 定义4个线程
[threads.append(my_thread_event(str(i), event)) for i in range(1,5)]

event.clear()

[t.start() for t in threads]

print("等待 5s ..")
time.sleep(5)

print("唤醒所有的线程")
event.set()


# condition
class Hider(threading.Thread):
    def __init__(self, name, cond):
        super().__init__()
        self.name = name
        self.cond = cond
        
    def run(self):
        time.sleep(1)
        self.cond.acquire()
        
        print(self.name + ": 我蒙上眼睛了")
        self.cond.notify()
        self.cond.wait()
        
        print(self.name + ": 我找到你了! ^_^")
        self.cond.notify()
        
        self.cond.release()
        print(self.name + ": 我赢了!")
        
class Seeker(threading.Thread):
    def __init__(self, name, cond):
        super().__init__()
        self.name = name
        self.cond = cond
        
    def run(self):
        self.cond.acquire()
        self.cond.wait()
        print(self.name + ": 我已经藏好了, 快来找我吧")
        self.cond.notify()
        self.cond.wait()
        
        self.cond.release()
        print(self.name + ": 被你找到了! 唉~~~")

cond = threading.Condition()
hider = Hider("hider", cond)
seeker = Seeker("seeker", cond)

hider.start()
seeker.start()


from queue import Queue

class student(threading.Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue
    def run(self):
        while True:
            msg = self.queue.get()
            if msg == self.name:
                print("{}: 到!".format(self.name))
                break

class Teacher(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        
    def call(self, student_name):
        print("老师: {}来了没有?".format(student_name))
        self.queue.put(student_name)
        
call_queue = Queue()

teacher = Teacher(call_queue)
xiaoming = student("xiaoming", call_queue)
xiaoliang = student("xiaoliang", call_queue)

xiaoming.start()
xiaoliang.start()

teacher.call("xiaoming")
time.sleep(1)
teacher.call("xiaoliang")



































