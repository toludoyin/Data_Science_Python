
# For loop (definite loop): it is used to iterate over an item of collection e.g a string
learning = ["youtube", "datacamp", "coursera", "udemy"]

for index, value in enumerate(learning):
    print(f"index  {str(index)} : {str(value)}")



# looping through a range and break to terminate a loop
total1 = 0
for value in range(1,100):
    if value % 3 or value % 5 == 0:
        total1 += value
    if total1 >= 150:
        break
print(total1)



# Iterating through or using a given number
list_ = [4, 6, 8]
for new_list1 in list_:
    new_list = " "
    for value in range(new_list1):
        new_list += "A"
    print(new_list)



# Nested loop; adding a loop inside another loop.
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")




# finding an average in a loop
count = 0
sum = 0
print('Before', count, sum)
for item in [23, 45, 81, 32, 12, 72, 90]:
    count = count + 1
    sum = sum + item
    print(count, sum, item)
print("After", count, sum, round(sum/count, 2))




# Dictionarys
key_value= {"name":"toludoyin", "level":"top", "class":1, "executive":True}
for key, value in key_value.items():
    print(f"This is my answer: {key}- {value}")




# function invokeation
def dictionary_():
    key_value= {"name":"toludoyin", "level":"top", "class":1, "executive":True}
    for s in sorted(key_value):
        print((s, key_value[s]))  #, end = " ")

def main():
    dictionary_()

if __name__ == "__main__":
    main()


