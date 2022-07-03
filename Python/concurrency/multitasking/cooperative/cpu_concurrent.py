


"""
The general concept of asyncio is that a single Python object, called the event loop,
controls how and when each task gets run. The event loop is aware of each task and 
knows what state it’s in.

In reality, there are many states that tasks could be in, but for now let’s imagine
a simplified event loop that just has two states.

The ready state will indicate that a task has work to do and is ready to be run,
and the waiting state means that the task is waiting for some external thing to finish,
such as a network operation.

An important point of asyncio is that the tasks never give up control without
intentionally doing so. They never get interrupted in the middle of an operation. 
This allows us to share resources a bit more easily in asyncio than in threading. 
You don’t have to worry about making your code thread-safe.

async and await

Now let’s talk about two new keywords that were added to Python: async and await.
In light of the discussion above, you can view await as the magic that allows the
task to hand control back to the event loop. When your code awaits a function call,
it’s a signal that the call is likely to be something that takes a while and that 
the task should give up control.

It’s easiest to think of async as a flag to Python telling it that the function about
to be defined uses await. There are some cases where this is not strictly true, like
asynchronous generators, but it holds for many cases and gives you a simple model while 
you’re getting started.

One exception to this that you’ll see in the next code is the async with statement, 
which creates a context manager from an object you would normally await. While the 
semantics are a little different, the idea is the same: to flag this context manager
as something that can get swapped out.

As I’m sure you can imagine, there’s some complexity in managing the interaction between
the event loop and the tasks. For developers starting out with asyncio, these details 
aren’t important, but you do need to remember that any function that calls await needs
to be marked with async. You’ll get a syntax error otherwise.

One of the cool advantages of asyncio is that it scales far better than threading.
Each task takes far fewer resources and less time to create than a thread, so creating 
and running more of them works well. This example just creates a separate task for each
site to download, which works out quite well.

The Problems With the asyncio Version

There are a couple of issues with asyncio at this point. You need special async versions
of libraries to gain the full advantage of asyncio. Had you just used requests for
downloading the sites, it would have been much slower because requests is not designed
to notify the event loop that it’s blocked. This issue is getting smaller and smaller
as time goes on and more libraries embrace asyncio.

Another, more subtle, issue is that all of the advantages of cooperative multitasking 
get thrown away if one of the tasks doesn’t cooperate. A minor mistake in code can 
cause a task to run off and hold the processor for a long time, starving other tasks 
that need running. There is no way for the event loop to break in if a task does not 
hand control back to it.
"""

import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
