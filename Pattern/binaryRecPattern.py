# 1 1 1 1
# 0 0 0 0
# 1 1 1 1
# 0 0 0 0
# 1 1 1 1
# 0 0 0 0

length = 4
heigth = 6

for i in range(heigth):
    for j in range(length):
        if i % 2 == 0:
            print("1 ", end="")
        else:
            print("0 ", end="")
    print()