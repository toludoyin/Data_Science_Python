# While loop (indefinite loop)
# while loop is a repeated if statement. it is use to execute a block of code multiple times until a particular condition is met
number = 1
no_limit = 5
while number < no_limit:
    print("$" * number)
    number += 1
print("submit \n")


counts = 6
while counts > 0:
    print(f'counts is: {counts}')
    counts -=1
else:
    print('blastoff \n')


while True:
    in_put = input("press any key:").lower()
    if in_put in ['a', 'e', 'i', 'o', 'u']:
        continue
    if in_put == 'next':
        break
    print(in_put)
print("Text inputed correctly\n")


# Number guessing game
import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f"Guess a number between 2 and {x}:"))
        if guess > random_number:
            print("Oops, number too high")
        elif guess < random_number:
            print("Number too low")
    else:
        print("Yay,you got the number correctly, Congrat! you won")

guess(10)

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    if largest is None:
        largest = num
    elif num > largest:
        largest = num


print("Maximum is", largest)
print("Minimum is", smallest)

# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = " "

#     while feedback != "C":
#         if low != high:
#             guess = random.randint(low,high)
#         else:
#             guess = low
#             feedback = input(f"Is {guess} too high(H), too low(L) or correct(C):").lower()
#         if feedback == "h":
#                 high = guess -1
#         elif feedback == "l":
#                 low = guess +1
#     print(f"Yoo.., the computer guessed the number{guess},correctly!.")

# computer_guess(10)