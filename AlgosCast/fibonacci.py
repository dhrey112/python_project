def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def user_input():
    input_ = int(input("Enter number: "))
    print(fib(input_))


user_input()
# f = fib(6)
# print(f)
