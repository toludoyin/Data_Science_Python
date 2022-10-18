#  list
courses = []
courses.extend([499, [17,45.6], 10.00, "pass", "secondclass", True]) # append multiple element
courses.append("firstclass")
course = [1,2,3,4]
print('Using operators to append multiple list: %s + %s' % (courses, course))  # list can contain any set of datatype

courses1 = courses[5]
print(courses1) # access list in list
courses.pop(-3)  # delete number in a list
print(courses)
print(courses[0:3])  # slicing
courses[1]=405  # replace
print(courses)

# swapping two element within a list
learning = ["youtube", "datacamp", "cousera", "udemy"]
studies = learning[0]
learning[0] = learning[-1]
learning[-1] = studies
print(learning)
print(learning.index("datacamp"))
learning[0], learning[-1] = learning[-1], learning[0]
print(learning)

first_draft = [3,10,4,7]  # use for-loop to append a list
second=[1.0,4,7,1]
for ss in second:
    first_draft.append(ss)
first_draft.sort()   # sort list
print(first_draft)

# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output. You can download the sample data at http://www.py4e.com/code3/romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word_split = line.split()
    for word in word_split:
        if word not in lst:
            lst.append(word)
        else: continue
print(sorted(lst))

# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for word in fh:
    word = word.rstrip()
    if not word.startswith('From '):
        continue
    words =word.split()
    count = count = count+1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")