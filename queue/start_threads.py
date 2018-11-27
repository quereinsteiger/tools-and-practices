# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:32:04 2018

@author: T.Schulz
"""

import read_queue
import write_queue

import threading
import queue
import time


#%%
if __name__ == '__main__':
    queue_main = queue.Queue()
    dat = list(range(11))
    thread1 = threading.Thread(target = write_queue.write, args = (dat, queue_main),name="tim1")
    thread1.daemon = True
    thread1.start()
    print(threading.enumerate(), "\n")
    time.sleep(2.0)
    thread2 = threading.Thread(target = read_queue.read, args=(queue_main,),name = "tim2")
    thread2.daemon = True
    thread2.start()
    print(threading.enumerate(), "\n")
    try:
        pass#while not queue_main.empty():
            #print(queue_main.get(block = False, timeout=5.0))
    finally:
        print('done')
        

        
        