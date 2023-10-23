'''Author: Abass- Tijani Modupe Aminat
Student ID: W0492257
Course: PROG1700
Project: Dinosaur Fried Chicken
Programming Language: Python 3
Date: Oct 23, 2023
'''
# Initialize variables
# Initial amount of fried chicken
total_fried_chicken = 20.00  
# Amount eaten on the first day
daily_eaten = 1.00 
# Day counter 
day = 1  

# Loop until there's no more fried chicken
while total_fried_chicken >= daily_eaten:
    # Output the amount of fried chicken eaten and remaining. .2f refers to a floating number in 2 decimal place
    print(f'Fried chicken eaten on day {day} = {daily_eaten:.2f}')
    # Update the remaining fried chicken
    total_fried_chicken -= daily_eaten 
    print(f'Fried chicken remaining: = {total_fried_chicken:.2f}')
    
    # Calculate the amount eaten on the next day
    if day != 7:  # On day 7, he gets a stomach ache and doesn't eat
        daily_eaten += daily_eaten * 0.05

    day += 1  # Increment the day counter

# Output the number of days it took to run out of fried chicken
print(f'It took {day - 1} days to run out of fried chicken.')
