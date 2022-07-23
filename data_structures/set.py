
# Set: are list with no duplicate entries. A set does not store data in order in which it is stored.

a = set()

a.add(2)
a.add(5)
a.add("garlic")
a
for x in a:
    print(x)


# when to use a set: when you want to remove a duplicate from a list
given_list = [3,3,5,11,11,4]
new_list = set()

for x in given_list:
    new_list.add(x)
# to sum the numbers
# total = 0
# for x in new_list:
#     total += x
print(new_list)


# reseting set back to a list
new_list1=[]
for x in new_list:
    new_list1.append(x)
print(new_list1)


# use intersection to search for common items in both list
a = set(['dam', 'tool', 'industry', 'fance'])
b = set(['dam', 'sharp', 'lust', 'merge', 'industry'])

print(b.intersection(a))

# distinct items
print(b.symmetric_difference(a))

# only common in each set
print(b.difference(a))

# union
print(b.union(a))

