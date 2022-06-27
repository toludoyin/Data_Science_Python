

def math(x):
    """function to calculate numbers"""
    return x ** 3 + 14

result = math(45)
print(f'Math result: {result}')
print('\n')



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
print('\n')
result2=convert(miles2)
print('\n')


# functions with two arguement
rice1=500
yam1=900

def food_price(rice, yam):
    price = (rice + yam)
    print(f'Total price of food: {price}')

    if price > 1500:
        return("move forward to the next shop")
    else:
        return("transfer")

food_price(rice1, yam1)

