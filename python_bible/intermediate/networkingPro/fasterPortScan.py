import socket
import threading
from queue import Queue

"""
In order to speed up the scanning process, we are going to use
multithreading . And to make sure that every port gets scanned and also that
no port is scanned twice, we will use queues
"""

target = "127.0.0.1"

q = Queue()
# fill up the port in a queue
for x in range(1, 50000):
    q.put(x)


# Function that does the port scanning
def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False


# function that gets all the ports from the queue in order to
# pass them to the portscan function and prints the result
def worker():
    while True:
        port = q.get()
        if portscan(port):
            print(f"Port {port} is open!")
    else:
        print(f"Port {port} is closed!")


# Using multithreading to speed up the process.
for x in range(500):
    t = threading.Thread(target=worker)
    t.start()
print("Port Scanning finished")
