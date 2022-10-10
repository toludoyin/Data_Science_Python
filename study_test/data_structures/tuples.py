
# tuples are immutable, can not be manipulated
empty_tuple = ()
numbers = (2,4,6,8,9,1)
values = (1,3,5,7)
print(type(numbers))

print(numbers[3]) # access a tuple
print(numbers + values) # add tuples
del numbers
print(numbers)  # this will give an error cause the variable no longer exist