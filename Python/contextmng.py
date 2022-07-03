#context managers
# allow allocation and release of memory

# with is a context manager, handles correct closing of file
with open('notes.txt', 'w') as file:
    file.write('some todoo...')


file = open('notes.txt', 'w')
try:
    file.write('some todoo...')
finally:
    file.close() # frees resource


#clearly with is better, much neater

from threading import Lock
lock = Lock()

# manually
lock.acquire()
#...
lock.release()

#using with
with lock:
    ...

# again with is better and safer


class ManagedFile:
    def __init__(self, filename, mode):
        print('init')
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        #print('exc:',exc_type, exc_value)
        print('exit')
        return True # prevents with from raising exception
    
with ManagedFile('notes.txt','w') as file:
    print('do some stuff...')
    file.write('somet odoo...')
    file.somemethod()
print('continuing...')

from contextlib import contextmanager

# now we can use this function in a with statement
@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w') # this is a generator
    try:
        yield f
    finally:
        f.close()


with open_managed_file('notes.txt') as f:
    f.write('some todooo...')