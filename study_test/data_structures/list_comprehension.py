
# todo: create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".
sentence = 'back in ethiopia we visited Adis ababa an the mago national park'

word_length = sentence.split()
word_list = [len(word) for word in word_length  if word != 'the']
print(word_list)

# todo: create a new list called "newlist" out of the list "numbers", which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(num) for num in numbers if num > 0]
print(newlist)

# todo: get square of value in given range
number = [value ** 2 for value in range(5, 20)]
print(number)

# todo: square given range from start: stop in a descending order
num = [value ** 2 for value in range(6, 0, -1)]
print(num)

# compute cartesian product of a and b
# eg: a=[1,2], b=[x,y]  = [1,x][1,y] and [2,x][2,y]

a = [1, 2, 4, 6]
b = [6, 12, 18, 24]
cartesian_product = [(x, y) for x in a for y in b ]
print(cartesian_product)