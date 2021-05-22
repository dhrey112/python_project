def collatz(number):

    while number != 1: 
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)

while True:
    try:
        input_ = int(input("Enter the number: "))
        collatz(input_)
        break
    except  ValueError:
        print("Invalid Input! Try again")
       
    
