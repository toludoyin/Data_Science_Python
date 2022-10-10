
# Set: are list with no duplicate entries. Set are unordered, mutable, unindexed and are mostly use for mathmatical operations

set_a = set()

set_a.add(2)  # add to set
set_a.add('python')
set_a.add('ephemeral')
set_a.remove(2) # remove item from set
for x in set_a:
    print(x)




given_list = [3,3,5,11,11,4]    # to remove a duplicate from a list
new_list = set()

for x in given_list:
    new_list.add(x)
# to sum the numbers
# total = 0
# for x in new_list:
#     total += x
print(f'duplicate removed {new_list}')


new_list1=[]  # reseting set back to a list
for x in new_list:
    new_list1.append(x)
print(new_list1)


# operations
a = set(['dam', 'tool', 'industry', 'fance'])
b = set(['dam', 'sharp', 'lust', 'merge', 'industry'])

print(f'intersection: {b & a}') # intersection
print(f'alternative intersection: {b.intersection(a)}\n')

print(f'union: {b | a}') # union
print(f'alternative union: {b.union(a)}\n')

print(f'difference: {b - a}') # difference
print(f'alternative difference: {b.difference(a)}\n')

print(f'symmetric difference: {b ^ a}') # symmetric difference
print(f'symmetric difference: {b.symmetric_difference(a)}')


