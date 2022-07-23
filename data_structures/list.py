

#  list
courses = [401, 407, 499, 1000, 412, 403]
max(courses)

# add to a list, a list can contain any set of datatype
courses.append("firstclass")
courses

# delete, the last number in a list
courses.pop(-1)
courses

# slicing
courses[0:3]


# replace
courses[1]=405
courses


# swapping two value/element within a list
learning = ["youtube", "datacamp", "cousera", "udemy"]

studies = learning[0]
learning[0] = learning[-1]
learning[-1] = studies

print(learning)

learning[0], learning[-1] = learning[-1], learning[0]
learning


