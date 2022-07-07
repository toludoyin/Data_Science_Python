
#  decorators makes it possible to make modification to callable object like functions, classes or methods

def my_decorator(func):
    def decorate():
        print('The learning curve')
        func()
    return decorate()



