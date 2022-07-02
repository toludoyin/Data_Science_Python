

#  list
courses = [401, 407, 412, 403, 499]
max(courses)


# To add to a list, a list can contain any set of datatype
courses.append("firstclass")
courses

# To delete, the last number in a list
courses.pop(1)
courses

# To select, slice
courses[3]

# To replace
courses[1]=405
courses


# Swapping two value/element within a list
learning = ["youtube", "datacamp", "cousera", "udemy"]
learning


studies = learning[0]
learning[0] = learning[-1]
learning[-1] = studies

print(learning)

learning[0], learning[-1] = learning[-1], learning[0]
learning