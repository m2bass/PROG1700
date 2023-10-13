'''
Author: Abass- Tijani Modupe Aminat
Student ID: W0492257
Course: PROG1700
Programming Language: Python 3
Date: Oct 12, 2023
'''
# import module
import random
# Prints the rules of the game. Performs string concatenation
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

#Global variable
invalid_attempts = 3
#it will continuously loop while the condition is true
while invalid_attempts > 0:
    # Local variable user_input
    user_input = input("Press 1 for Rock, 2 for paper, 3 for scissors:")
    # validate the input to ensure the program does not have invalid input
    # return true if a digit is entered otherwise return false
    if user_input.isdigit():
        # Ensures user input is not equal to zero and not greater than 3 
        if 0 < int(user_input) < 4:
            # cast to an integer
            user_input = int(user_input)
            # Computer chooses randomly any number among 1 , 2 and 3. Using randint method  
            computer_value = random.randint(1,3)
            print("Computer chooses:", computer_value)
            # 1, 2, 3 number only
            if user_input != computer_value:
            # calculate the computer's value  (the last number 1 shows how many turns)
                if user_input == 1 and computer_value == 3 or user_input == 2 and computer_value == 1 or user_input == 3 and computer_value == 2:
                    print("User Wins!") 
                else:
                    print("Computer Wins!")     
            else:
                print("It is a draw!")
        else:     
            print("Enter a valid choice please")
            invalid_attempts = invalid_attempts - 1
            print("You have", invalid_attempts,"attempts")
    else:         
        print("Invalid Input")     
else:
    print("Thanks for playing!")

