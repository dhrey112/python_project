import threading, time

"""Without Locking"""
x = 8192


def halve():
    global x
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("END!")


def double():
    global x
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("END!")


t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

# t1.start()
# t2.start()

"""With Locking"""
lock = threading.Lock()


def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("END!")
    lock.release()


def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("END!")
    lock.release()


t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)
t1.start()
t2.start()
