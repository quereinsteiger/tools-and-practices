# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:57:07 2018

@author: T.Schulz
"""

#import matplotlib.pyplot as plt
#import queue
#import time

def read(queue0, storage=[]):
    try:
        while True:
            storage.append(queue0.get(timeout=5))
            print('read {}'.format(storage))
            #return storage
    except:
        print("empty")

        

if __name__ == '__main__':
    # Dies ist ein Test für das read_queue Modul
    for i in range(3):
        data=read(i)
        print(data)
    plt.plot(data)