'''
Author: Abass- Tijani Modupe Aminat
Student ID: W0492257
Course: PROG1700
Programming Language: Python 3
Date: Oct 17, 2023
Project: Guessing Game
'''

import random

# define range and max_attempts
lower_bound = 1
upper_bound = 10
max_attempts = 5

# generate the secret number
secret_number = random.randint(lower_bound, upper_bound)

name = input("What is your name?")
print('Hi,', name, 'this is a guessing game. I will guess a number from 1 to 10, and you will attempt to guess my number. You have 5 attempts of guessing my number to win.')

# Get the user's guess
def get_guess(attempts):
    while True:
        try:
            guess = int(input(f"What is your guess, {lower_bound} - {upper_bound}? "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        # Exits the game after 5 invalid inputs.
        attempts += 1
        if attempts > 3:
            print("Too many incorrect attempts. Exiting the game.")
            exit()

# Validate guess
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Your guess is too low."
    else:
        return "Your guess is too high."

# track the number of attempts, detect if the game is over
def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess(attempts)
        result = check_guess(guess, secret_number)

        if result == "Correct":
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} tries!")
            won = True
            break
        else:
            print(f"{result}. Try again!")

    if not won:
        print(f"You guessed the number in 3 tries! The secret number is {secret_number}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()
