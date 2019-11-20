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
        self.cond.release()
        
class seeker(threading.Thread):
    def __init__(self, name, cond):
        super().__init__()
        self.name = name
        self.cond = cond
        
    def run(self):
        self.cond.acquire()
        self.cond.release()
        