# commennts

# import modules here
import random

#Global variable
invalid_attempts = 3
#it will continuously loop while the codition is true
while invalid_attempts > 0:
    # Local variable user_input
    user_input = input("Press 1 for Rock, 2 for paper, 3 for scissors:")
    # validate the input to ensure the program does not have invalid input
    # return true if a digit is entered otherwise return false
    if user_input.isdigit():
        if len(user_input) == 1:
            # cast to an integer
            user_input = int(user_input)
            computer_value = random.randint(1,3)
            print(computer_value)
            # 1, 2, 3 number only
            if user_input != computer_value:
            # calculate the computer's value  (the last number 1 shows how many turns)
                if user_input == 1 and computer_value == 3 or user_input == 2 and computer_value == 1 or user_input == 3 and computer_value == 2:
                    print("User Wins!") 
                else:
                    print("Computer Wins!")     
            else:
                print("Tie  Game")
        else:     
            print("Please enter a single digit")
            invalid_attempts = invalid_attempts - 1
            print("You have", invalid_attempts,"attempts")
    else:         
        print("Invalid Input")     
else:
    print("You do not have any attempts left!")
# main

