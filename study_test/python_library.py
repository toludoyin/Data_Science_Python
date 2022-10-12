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