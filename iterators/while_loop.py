
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



