
# Task question:
# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. --> week5(coursera --programming for everyone)

# FIRST approach using numpy library
score = input("Enter Score: ")
iscore = float(score)

import numpy as np
for num in np.arange(0, 1.0, 0.1):
    number = num
if iscore > number:
    print('number out of range')
else:
    if iscore >= 0.9:
        print('A')
    elif iscore >= 0.8:
        print('B')
    elif iscore >= 0.7:
        print('C')
    elif iscore >= 0.6:
        print('D')
    elif iscore < 0.6:
        print('F')




# SECOND approach using generator functions
score = input("Enter Score: ")
iscore = float(score)

def num_loop():
    """function to generate numbers between 0 and 1.0"""
    num = 0
    while num <= 1.0:
        yield num
        num += 0.1
for number in num_loop():
    range_num = number

# compare user input with number in range
if iscore > range_num:
    print('number out of range')
else:
    if iscore >= 0.9:
        print('A')
    elif iscore >= 0.8:
        print('B')
    elif iscore >= 0.7:
        print('C')
    elif iscore >= 0.6:
        print('D')
    elif iscore < 0.6:
        print('F')

