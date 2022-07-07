
# For loop: it is used to iterate over an item of collection e.g a string
learning=["youtube", "datacamp", "cousera", "udemy"]

for index, a in enumerate(learning):
    print(f"index  {str(index)} : {str(a)}")

total1=0
for i in range(1,100):
    if i % 3 or i % 5 == 0:
        total1+=i
print(total1)

# Iterating through or using a given number
list=[4,6,8]
for new_list1 in list:
    new_list = " "
    for x in range(new_list1):
        new_list += "A"
    print(new_list)


# Nested loop; adding a loop inside another loop.
# break;is use to terminate a loop
for x in range(2):
    for y in range(3):
        print(f"({x},{y})")


# Dictionary
key_value= {"name":"toludoyin", "level":"top", "class":1, "executive":True}
for key,value in key_value.items():
    print(f"This are my answers: {key}- {value}")

# to sort by keys in a dict
for s in sorted(key_value):
    print(s,(key_value[s]))


# function calling
def dictionary():
    key_value= {"name":"toludoyin", "level":"top", "class":1, "executive":True}
    for s in sorted(key_value):
        print((s,key_value[s]),end = " ")

def main():
    dictionary()

if __name__=="__main__":
    main()
