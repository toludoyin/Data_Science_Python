from functools import partial
def multiply(x, y, z):
    return x*y + y*z/x

new_func = partial(multiply, 2)
print(new_func(5,4))