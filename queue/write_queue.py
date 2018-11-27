# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:14:07 2018

@author: T.Schulz
"""

import queue
import time

def write(items, q):
    for item in items:
        q.put(item**2)
        print("I'm thread Tim1")
        time.sleep(0.5)
    return


if __name__ == '__main__':
    # Sequenz zum Testen von write_gueue()
    queue0 = queue.Queue() 
    write([1,2,3],queue0)
    
    while not queue0.empty():
        print(queue0.get())
    print('done')

#%%
def send(queue, message_nums=10):
    for n in range(message_nums):
        time.sleep(0.1)
        queue.put('message number: {}'.format(n))