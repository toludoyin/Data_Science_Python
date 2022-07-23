

#  list
courses = [4.1, 407, 499, 1000, 412, [1.2, 45.6]]
courses.append("firstclass")  # list can contain any set of datatype
print(courses)

courses.extend(["pass", "secondclass"]) # append multiple element
print(courses)

courses1 = courses[5]
print(courses1[0]) # access list in list

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


first_draft = [3,10,4,7,5,6]
first_draft.sort()   # sort list
print(first_draft)
sec_draft = [4,5,7,8]

