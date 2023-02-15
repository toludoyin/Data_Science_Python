# exceptions are python solutions to error
rawstr = input('Enter a number: ')
try:
    int_val = int(rawstr)
    if int_val > 0:
        print('Great')
    else:
        print('Not a number')
except:
    print('input not identify')

# calculate rate and hour
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    fh = float(hrs)
    fr = float(rate)
    if fh > 40:
        hr = fh * fr
        com_hr = (fh - 40) * (fr * 0.5)
        end_hr = hr + com_hr
        print(end_hr)
    else:
        hr = fh * fr
        print('Pay:', hr)
except:
    print('input is not a number')
    quit()