from multiprocessing import Process, Value, Array, Lock
from threading import Thread
import os
import time


def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

processes = []
threads = []
num_threads = 10
num_proceses = os.cpu_count()
print(num_proceses)

# create threads
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# create processes
for i in range(num_proceses):
    p = Process(target=square_numbers)
    processes.append(p)

# start threads
for t in threads:
    t.start()

#start processes
# for p in processes:
#     p.start()

# start threads
for t in threads:
    t.join()

# # join
# for p in processes:
#     p.join()

print('end main')

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value +=1


if __name__ == "__main__":
    lock = Lock()
    shared_array = Array('d', [0.0,100.0,200.0])
    shared_number = Value('i',0)

    print('Array at begining is', shared_array[:])
    print('Number at begining is', shared_number.value)

    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at end is ',shared_number.value)
    print('Array at end is', shared_array[:])

