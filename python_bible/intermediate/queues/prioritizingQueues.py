import queue

q = queue.PriorityQueue()

q.put((8, "Some string"))
q.put((1, 2023))
q.put((90, True))
q.put((2, 10.23))

while not q.empty():
    print(q.get())

    #  If you
    # only want to access the actual value, you need to address the index one
    # because it is the second value of the tuple.
    print(q.get()[1])
