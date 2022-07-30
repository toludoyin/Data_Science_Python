
# functions with single arguement
def math(x):
    """function to calculate numbers"""
    return x ** 3 + 14

result = math(45)
print(f'Math result: {result}' + '\n')




# functions with an already predefined declared variable arguement
miles1 = 52
miles2 = 15

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
    if others.get('action') == 'sum':
        print('The sum is: %d' %(product_a + product_b + product_c))

    if others.get('rank') == 'product_a':
        return product_a

result = product(1,2,3, action = 'sum', rank = 'product_a')
print('Rank: %d' %(result))




# Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more) The foo function must return the amount of extra arguments received. The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.

def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs['magicnumber'] == 7

if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")

