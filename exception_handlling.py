
# python solutions to error

def do_something(n):
    print(n)

def catch_this():
    list_num = (1,2,3,4,5,6)

    for a in range(20):
        try:
            do_something(list_num[a])
        except IndexError:
            do_something(0)

catch_this()