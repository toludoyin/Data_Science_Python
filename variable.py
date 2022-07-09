
# datatypes
strings_ = 'Gender'
float_ = 3.14
integers_ = 654
booleans_ = True or False
# complex_ = 4 + 123y
dictionary_ = {'name': 'jam jam',
               'age': 100,
               'married': False}
set_ = {'name', 35, True, 13.6}
list_ = ['name', 35, True, 13.67]
tuple_ = ('name', 35, True, 13.67)
print(type(set_))




# remainder = %
# operation evaluation rule; parenthesis, exponential, (multiplication, division, remainder), (addition, subtraction) --> left >> right
number = 13 + 8 * 9 / 4 ** 3
print("Expression result:", number)

# assigning variables to value and expressions to solve a quadratic equation
import math
a = 6  # assignment statement
b = 10
c = 12
quadratic_equation = -b +- (math.sqrt(b ** 2) - (4 * a * c))/ 2 * a  #expression
print("The quadratic equation result is %s" % quadratic_equation)




# swapping variables
adapter = "postilion"
intent = "reversal"

bank = adapter
adapter = intent
intent = bank
print(intent)




# input finction to welcome user
intro = input("what is your name? ").title()
intro1 = input("Let's get to know you, what is your favorite programming language? ").upper()
print(f"Welcome {intro}. We love your favorite programming language {intro1}.")



# an input function to give users their toatal pay based on their imput
hrs = input("Enter Hours to learn: ")
rate = input("Enter Rate: ")
print("Pay:", float(hrs) * float(rate))
