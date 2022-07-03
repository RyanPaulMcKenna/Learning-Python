import concurrent.futures
import threading
import requests
import time

"""
Threading in python is an example of pre-emptive multitasking
in which the operating system can pre-empt your thread to make the switch.
The operating system can interrupt each thread at ny time to start running 
a different thread. 
Simpler to code than cooperative multitasking but has the disadvantage of
being able to interrupt in the middle of a python statement such as x = x + 1.

each thread needs to be thread safe so that the OS doesn't start changing
another threads data. request.Session() for example is not thread-safe.

There are several strategies for making data accesses thread-safe depending
on what the data is and how you’re using it. One of them is to use thread-safe
data structures like Queue from Python’s queue module.
These objects use low-level primitives like threading.Lock to ensure that only
one thread can access a block of code or a bit of memory at the same time.
You are using this strategy indirectly by way of the ThreadPoolExecutor object.

Another strategy to use here is something called thread local storage. 
threading.local() creates an object that looks like a global but is specific
to each individual thread. In your example, this is done with thread_local
and get_session():

too many threads will erase any time savings.


Well, as you can see from the example, it takes a little more code to make this happen, and you really have to give some thought to what data is shared between threads.

Threads can interact in ways that are subtle and hard to detect. 
These interactions can cause race conditions that frequently result in random,
intermittent bugs that can be quite difficult to find. Those of you who are unfamiliar
with the concept of race conditions might want to expand and read the section below.

Race conditions are an entire class of subtle bugs that can and frequently
do happen in multi-threaded code. Race conditions happen because the programmer
has not sufficiently protected data accesses to prevent threads from interfering
with each other. You need to take extra steps when writing threaded code to ensure
things are thread-safe
"""

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")