# print 1 to 100
# multiple of 3 = 'Fizz'
# Multiple of 5 = 'Buzz'
# multiple of 3 and 5 = 'FizzBuzz'


i = 0
for i in range(i, 100):
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')

    else:
        print(i)
