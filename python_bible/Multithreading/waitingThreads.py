import threading

def function():
    for x in range(1000):
        print("Hello World")


t1 = threading.Thread(target=function)
t1.start()
t1.join(0.0001) # we wait for the thread to finish before we move on with the last print statement.
print("This is the End!")