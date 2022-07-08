
# python solutions to error

astr = 'hello world'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '456'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)





rawstr = input('Enter a number: ')
try:
    int_val = int(rawstr)
except:
    int_val = -1
if int_val > 0:
    print('Great')
else:
    print('Not a number')





def do_something(n):
    print(n)

def catch_this():
    list_num = (1,2,3,4,5,6)

    for a in range(10):
        try:
            do_something(list_num[a])
        except IndexError:
            do_something(0)

catch_this()


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    fh = float(hrs)
    fr = float(rate)
except:
    print('input is not a number')
    quit()

if fh > 40:
    hr = fh * fr
    com_hr = (fh - 40) * (fr * 0.5)
    end_hr = hr + com_hr
    print(end_hr)
else:
    hr = fh * fr
    print('Pay:', hr)


