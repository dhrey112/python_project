import threading
import time

path = "text.txt"
text = ""


def read_file():
    global text, path
    while True:
        with open(path) as file:
            text = file.read()
        time.sleep(3)


def print_loop():
    global text
    for x in range(30):
        print(text)
        time.sleep(1)


t1 = threading.Thread(target=read_file, daemon=True)
t2 = threading.Thread(target=print_loop)

t1.start()
t2.start()