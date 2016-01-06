"""
from multiprocessing import Process
import os


def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'

"""
"""
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print 'Task %s runs %.2f seconds.' % (name, (end-start))

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(3) # how many processes allowed, this means we can open 3 processes in the same time
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocessing done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
"""

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for value in range(10):
        print 'Put (%s) to queue...' % value
        q.put(value)
        time.sleep(0.2)

def read(q):
    while True:
        try:
            value = q.get(True,2)
        except:
            print 'q is Empty!'
            break
        print 'Get (%s) from queue.' % value
        time.sleep(0.3)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()