# This is a guess game.
import random

print("Hello, what is your name?")
name = input(">> ")
print(f"Welcome, {name} to know your guessing skill")
print(f"Well, {name}, I am thinking of a number between 1 and 30")
secret_number = random.randint(1, 20)

for number_of_guess in range(1, 6):
    print("What is your guess?")
    guess = int(input(">> "))

    if guess < secret_number:
        print(f"{guess} is lower than the secret number")
    elif guess > secret_number:
        print(f"{guess} is greater than the secret number")
    else:
        break

if guess == secret_number:
    print(f"Good job, {name}, you guess the number in {number_of_guess} guessed ")
else:
    print(f"Oops! The number I was thinking is {secret_number}")