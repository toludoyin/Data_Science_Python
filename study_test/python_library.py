# QUESTION
# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
new_text = text.find(":")
float_value = text[new_text+1:]
clean_float = float_value.strip()
print(float(clean_float))

# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name
file= input("enter your filename:")
try:
    filename = open(file)
    readfile = filename.read()
except:
    print("File is not found")
    quit()
word = "X-DSPAM-Confidence:"
result=0
count = 0
for line in filename:
    if line.startswith(word):
        l = len(word)
        number = float(line[l+1:])
        result = result + number
        count = count + 1
        continue
try:
    avg = result/count
except ZeroDivisionError:
    avg =0
print("Average spam confidence:", avg)

fruit = ['orange mango pineapple watermelon']
fruits =fruit.split()
print(fruits)

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
