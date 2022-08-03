
# functions with single arguement
def math(x):
    """function to calculate numbers"""
    return x ** 3 + 14

result = math(45)
print(f'Math result: {result}' + '\n')



# functions with an already predefined declared variable arguement
miles1 = 52
miles2 = 2

def convert(miles):
    kilogram = 1.6 * miles
    print(f'miles kilogram: {kilogram}')

    if kilogram > 20:
        print('big miles')
    else:
        print('underweight')

result1=convert(miles1)

result2=convert(miles2)



# multiple function and keyword arguement
def product(product_a, product_b, product_c, **others):
    if others.get('addition') == 'sum':
        print('The sum is: %d' %(product_a + product_b + product_c))

    if others.get('order') == 'product_a':
        return product_a

result = product(1,2,3, addition = 'sum', order = 'product_a')
print('Order: %d\n' %(result))




# Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more) The no1 function must return the amount of extra arguments received. The no2 must return True if the argument with the keyword number is worth 7, and False otherwise. from learnpython.com

def no1(a, b, c, *args):
    return len(args)

def no2(a, b, c, **kwargs):
    return kwargs['number'] == 7

if no1(1, 2, 3, 4) == 1:
    print("Good.")
if no1(1, 2, 3, 4, 5) == 2:
    print("Better.")
if no2(1, 2, 3, number=6) == False:
    print("Great.")
if no2(1, 2, 3, number=7) == True:
    print("Awesome!")

