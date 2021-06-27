import threading

"""
Another way to build our threads is to create a class that inherits the Thread
class.
"""


class MyThread(threading.Thread):
    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        for x in range(100):
            print(self.message)


mt1 = MyThread("This is my thread Message")
mt1.start()
