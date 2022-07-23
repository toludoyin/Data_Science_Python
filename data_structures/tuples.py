
# tuples are immutable, can not be manipulated
empty_tuple = ()
numbers = (2,4,6,8,9,1)
print(type(numbers))

print(numbers[3]) # access a tuple
del numbers
print(numbers)  # this will give an error cause the variable no longer exist