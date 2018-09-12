from Queue import Queue
import time
import random
import threading

q = Queue(maxsize=3)

task_queue = range(1,100)


test_queue = range(1,10)
success_list = []


def producer(name):
    while len(task_queue) > 0:
        if q.qsize() < q.maxsize:
            task = task_queue.pop()
            print('put into %s queue a new task %d'%(name,task))
            q.put(task)
            time.sleep(random.random())
    q.put('finish')
    print('consumer finish')


# class Watcher(threading.Thread):
#     while len(success_list) < len(task_queue):
#         pass


def consumer(name):
    over = True
    while over:
        task = q.get()
        if task == 'finish':
            over = False
        else:
            time.sleep(random.random())
            print('consumer %s get queue a new task %d' % (name, task))
            success_list.append(task)
    print('consumer finish')


def test():
    print task_queue
    print len(task_queue)
    while len(task_queue) > 0:
        for i in test_queue:
            print i, len(test_queue)
            time.sleep(0.1)
        print 'task_queue',len(task_queue)


def test1():
    while len(test_queue) > 0:
        test_queue.pop()
        time.sleep(0.5)


def main():
    pro = threading.Thread(target=producer, args=('AA',))
    con = threading.Thread(target=consumer, args=('BBB',))
    pro.start()
    con.start()
    pro.join()
    con.join()


def test3():
    a = threading.Thread(target=test1)
    a.start()
    test()


if __name__ == '__main__':
    test3()
