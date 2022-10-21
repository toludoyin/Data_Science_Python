# tuples are immutable, can not be manipulated
empty_tuple = ()
numbers = (2,4,6,8,9,1)
values = (1,3,5,7)
print(type(numbers))

print(numbers[3]) # access a tuple
print(numbers + values) # add tuples
del numbers
# print(numbers)  ## this will give an error cause the variable no longer exist

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    if "From:" in line:
        continue
    if "From" in line:
        word_split = line.split()
        hour = word_split[5].split(":")[0]
        dic[hour] = dic.get(hour, 0)+1

lst = list()
for key, value in dic.items():
    lst.append([key, value])
lst = sorted(lst, reverse= True)

for key, value in sorted(lst):
    print(key, value)