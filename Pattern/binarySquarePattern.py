#TODO 1 1 1 1
#     0 0 0 0
#     1 1 1 1
#     0 0 0 0

length = 4

for i in range(length):
    for j in range(length):
        if i % 2 == 0:
            print("0 ", end="")
        else:
            print("1 ", end="")
    print()