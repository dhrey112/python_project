import threading
import time

"""
Sometimes we don’t want to completely lock a resource but just limit it to a
certain amount of threads or accesses.
"""

semaphore = threading.BoundedSemaphore(value=5)


def access(thread_num):
    print("{}: Trying access...".format(thread_num))

    semaphore.acquire()
    print("{}: Access granted!".format(thread_num))
    print("{}: Waiting 5 seconds...".format(thread_num))

    time.sleep(5)

    semaphore.release()
    print("{}: Releasing!" .format(thread_num))


for thread_number in range(10):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
