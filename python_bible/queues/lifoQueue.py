import queue

q = queue.LifoQueue()

numbers = [1, 2, 3, 4, 5]

for x in numbers:
    q.put(x)

while not q.empty():
    print(q.get())
