'''Author: Abass- Tijani Modupe Aminat
Student ID: W0492257
Course: PROG1700
Project: Dictionaries
Programming Language: Python 3
Date: Nov 11, 2023
'''
# Function to sum
def returnSum(student_scores):
    sum = 0
    for i in student_scores.values():
        sum = sum + i
    return sum

# Function for total value
def returnTot(student_scores):
    total = 0
    for i in student_scores.values():
        total = total + 1
    return total
 
# Creating a dictionary showing students' names and scores
student_scores = {
    'Alice' : 90,
    'Bob' : 85,
    'Charlie' : 78,
    'David' : 92,
    'Eve' : 88
    }

# Print the initial dictionary
for student in student_scores:
    print(f'{student} : {student_scores[student]}')

# Calculate and print the average test score of all the students
print("Average: ", returnSum(student_scores)/returnTot(student_scores))

# Prompts user to enter student's name
name = input("Enter Student\'s name: ")

# Checks if student exists in the dicitionary
if name in student_scores:
    print(f'Name: {name} | Score: {student_scores[name]}')
else:
    print("Student's name not found!")

# Update the record
updated = input("Enter new student\'s name: ")
score = int(input("Enter score: "))

student_scores[updated] = score
for student in student_scores:
    print(f'{student} : {student_scores[student]}')

# Prompt user to delete a student record
remove = input('Enter student record to delete: ')

if remove in student_scores:
   del student_scores[remove]
else:
    print(f'Student name {remove} not in record')

for student in student_scores:
    print(f'{student} : {student_scores[student]}')

# Calculate and print the highest score and student
max_value = max(student_scores.values())     
max_pair = max(student_scores, key=student_scores.get)
print("Student: ", max_pair, "| Score: ", max_value)

