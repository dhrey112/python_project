import threading

event = threading.Event()


def function():
    print("Waiting for an event\n")
    event.wait()
    print("Continuing!")


thread = threading.Thread(target=function)
thread.start()

x = input("Trigger event? ")
if x == "yes":
    event.set()
