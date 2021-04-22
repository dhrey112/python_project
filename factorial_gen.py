def product(a, b):
    return a * b


def factorial_gen():
    i = 1
    n = i
    while True:
        output = product(n, i)
        yield output
        i += 1
        n = output

fact = factorial_gen()
num = 5
for i in range(num):
    print(next(fact))