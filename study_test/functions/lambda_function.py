# anonymous function
a=5
b=6
result = lambda x,y: x*y/x
final = result(a,b)
print(final)

# multiply number by 8 in range
print(list(map(lambda number: number ** 8, range(5))))

# applying a function to a list
number_tank= [1,2,3,4]
for n in number_tank:
    result = lambda n: n **3
    print(result(n))

# question: check if a number in the given list is odd. Print "True" if the number is odd or "False" if not for each element.
l = [2, 4, 7, 3, 14, 19]
for odd_num in l:
    result = lambda odd_num: odd_num % 2 > 0
    print(result(odd_num))

#  get list of boolean the the below condition
stocks = ['Amazon', 'Netflix', 'Google', 'Facebook','Apple']
print(list(map(lambda x: x[0] == 'G' or x[-1] == 'e', stocks)))

# get list of filtered condition
print(list(filter(lambda x: x[0] == 'A', stocks)))