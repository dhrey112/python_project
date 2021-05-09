"""
    *
    * * *
    * * * * *
    * * * * * * *
"""

num = int(input("Enter number of row: "))

k = 1
for i in range(1, num+1):
    for j in range(1, k+1):
        print("* ", end="")
    print()
    k += 2
