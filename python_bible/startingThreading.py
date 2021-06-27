import threading


def hello():
    print("Hello World!")


t1 = threading.Thread(target=hello)
t1.start()
