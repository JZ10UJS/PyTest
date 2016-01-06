#!usr/bin/python
# coding:utf-8

import time, sys, Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_host = '192.168.1.106'
port = 5000
print 'connect to server %s:%s...' % (server_host, port)

m = QueueManager(address=(server_host, port), authkey='abc')

m.connect()

print 'connect success...'

task = m.get_task_queue()
result = m.get_result_queue()

while True:
    try:
        n = task.get(timeout=1)
        print 'run task %d * %d...' % (n, n)
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print ('task Queue is empty')
        break

print 'worker exit.'
