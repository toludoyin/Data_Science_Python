
# While loop
# while loop is a repeated if statement. it is use to execute a block of code multiple times until a particular condition is met

number = 1
no_limit = 5
while number < no_limit:
    print("$" * number)
    number += 1
print("submit")




counts = 6
while counts > 0:
    print(f'counts is: {counts}')
    counts -=1
else:
    print('blastoff')




error = 50
while error > 1:
    error = error/4
    print(error)




# Number Guessing Game
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
        print("Yay,you got the number correctly,Congrat! you won")


guess(15)




def computer_guess(x):
    low = 1
    high = x
    feedback = " "

    while feedback != "C":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
            feedback = input(f"Is {guess} too high(H), too low(L) or correct(C):").lower()
        if feedback == "h":
                high = guess -1
        elif feedback == "l":
                low = guess +1
    print(f"Yoo.., the computer guessed the number{guess},correctly!.")


computer_guess(10)