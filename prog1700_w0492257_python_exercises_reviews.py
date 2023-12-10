'''
Author: Abass- Tijani Modupe Aminat
Student ID: W0492257
Course: PROG1700
Project: Create a simple Algorithm using the program flowchart and pseudocode
Programming Language: Python 3
Date: Sept 26, 2023


'''

# Create two string variables, str1 and str2, and concatenate them into a third variable result_str.
str1 = "The big browm"
str2 =  " fox fell off the cliff"
result_str =  str1 + str2
print(result_str)

# Given a string sentence, extract and print the first five characters.
chr = "The dancing bear"
print(chr[0:6])

# Create a string that includes variables. Use string formatting to insert values into the string.
coup = 2
candl = "candle light dinners were lit"
print(f"The {coup} {candl}")

# Using a for loop, print the numbers from 1 to 10.
num = 0
for num in range(1,11):
    # The end parameter in the print function is used to add any string. Hence making the numbers print horizontally while adding spaces
    print(num, end=' ')
# Add a break line
print()    

# Write a function to calculate the factorial of a number using a while loop.
''' METHOD 1
def factorial(num):
    result = 1
    while num > 0:
        result = result * num
        #result = *= num
        num = num -1
    return result
print(factorial(5))'''
# METHOD 2
import math
print(math.factorial(5))

# Create two sets, set1 and set2, and find and print their intersection.
'''' METHOD 1 
var3 = var1.intersection(var2)
print(var3)'''
# METHOD 2
#Using nested looping method union=| , intersection= & , difference= -
var1 = {1, 2, 3, 4, 5}
var2 = {6, 4, 1, 7, 8}

intersection_set = var1 & var2
print(intersection_set)

union_set = var1 | var2
print(union_set)

difference_set = var1 - var2
print(difference_set)

# List Operations:Sum, Average, Maximum and Minimum values

numbers = [11, 12, 14, 13, 18]

sum1 =  sum(numbers)
print(sum1)

avg = sum1/len(numbers)
print(avg)

maximum = max(numbers)
print(maximum)

minimum = min(numbers)
print(minimum)

# Generate a list of squares of numbers from 1 to 10 using list comprehension.
squares = [x**2 for x in range(1,11)]
print(squares)

# Create a tuple with three values. Unpack the tuple into three variables and print them
vegetables_tuples = ("Carrots", "lettuce", "onions")
(orange, green, purple) = vegetables_tuples
print(orange)
print(green)
print(purple)

# Create a dictionary representing a person with keys like 'name', 'age', and 'city'. Print each key-value pair.dictt
dict1 = {"name": "David",
        "Age": 20,
        "City": "California"}
for k, v in dict1.items():
    print(f'{k.capitalize()} : {v}')

# Create a nested dictionary representing information about students and their grades. Print the average grade for each student.
students_data = {
    'James': {
        'Maths': 50,
        'English': 40,
        'Chemistry':48
    }, 
     'Sarah': {
         'Maths': 70,
         'English': 50,
         'Chemistry': 95
     },
     'Jacob': {
         'Maths': 84,
         'English': 94,
         'Chemistry': 90
     }
}
for student, grades in students_data.items():
    average_grade = sum(grades.values())/len(grades)
    print(f"{student}'s average grade: {average_grade}")

# Write a function that takes two arguments and returns their sum.
def  my_letters(a,b):
    print('Sum:', a + b )

my_letters(5,7)

# Modify the previous function to have default values for the arguments.
def my_letters(a = 3, b = 1):
    print('Sum:', a + b )
my_letters()

# File Writing: Write a list of strings to a new text file named 'output.txt'.
data_insert = ["Looking", "into", "space"]
try:
  with open("output.txt", "w") as file: 
      for d in data_insert:
          file.write(d + "\n") 
except IOError:
    print("An error occured writing the file")
# Pauses the program to view the result
print(input("...press return to continue"))

# File Reading: Read a text file named 'output.txt' and print its contents line by line.
try:
    with open("output.txt", "r") as thefile:
        for eachline in thefile:
            print(eachline.strip())
except FileNotFoundError:
    print("File cannot be found! Verify if file exists")

# Read a text file named 'output.txt and store each line in a list
newlist = []
try:
    with open("output.txt", "r") as thefile:
        for eachline in thefile:
            newlist.append(eachline.strip())
    print(thefile)
except FileNotFoundError:
    print("File not found.")




