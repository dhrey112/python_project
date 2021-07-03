import queue

q = queue.Queue()

for x in range(5):
    q.put(x)

for x in range(5):
    print(q.get())
