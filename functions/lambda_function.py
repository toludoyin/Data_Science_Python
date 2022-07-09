
# anonymous function

#multiply number by 8 in range
list(map(lambda number: number ** 8, range(5)))


#  get list of boolean the the below condition
stocks = ['Amazon', 'Netflix', 'Google', 'Facebook','Apple']
list(map(lambda x: x[0] == 'G' or x[-1] == 'e', stocks))

# get list of filtered condition
list(filter(lambda x: x[0] == 'A', stocks))


# question: check if a number in the given list is odd. Print "True" if the number is odd or "False" if not for each element.
l = [2, 4, 7, 3, 14, 19]
for odd_num in l:
    result = lambda odd_num: odd_num % 2 > 0
    print(result(odd_num))


