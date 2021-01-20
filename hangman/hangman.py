import random
import time

print("\nWelcome to Hangman game\n")
name =input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

# Define the main function

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = [["january","java","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]]