from threading import Thread, Lock, current_thread
import time
from queue import Queue

database_value = 0


def increase(lock):
    global database_value

#   with lock: ##alternative method doesn't require other lock methods
    lock.acquire()
    local_copy = database_value

    #processing
    local_copy +=1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()

def worker(q, lock):
    while True:
        value = q.get()

        #processing...
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == "__main__":

    lock = Lock()
    print('start value', database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


    print('end value', database_value)

    padlock = Lock()
    q = Queue()

    # q.put(1)
    # q.put(2)
    # q.put(3)

    # # 3, 2 1 ->
    # first = q.get()
    # print(first)
    # q.task_done()
    # q.join()

    num_threads = 10
    # daemon thread dies when the main thread dies
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,padlock))
        thread.daemon=True
        thread.start()

    for i in range(1,21):    
        q.put(i)
    
    q.join()


    print('end main')

