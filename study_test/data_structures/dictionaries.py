dictionary_ = {'name': 'jam jam',
               'age': 100,
               'married': False,
               'job': 'data scientist'
               }
dictionary_['nationality'] = 'san-francisco' # add to dict
for key, value in dictionary_.items():
    print(f'Users details: {key}, {value}')
print(dictionary_.get('age', 0)) # to access a dict

key = ['no_1', 'no_2', 'no_3', 'no_4'] # convert lists to dict
values = [3, 10, 4, 7]
result = dict(zip(key, values))
print(result)

# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
db = list()
for word in handle:
    word= word.strip()
    if not word.startswith('From:'):
        continue
    word = word.split()
    word = word[1]
    db.append(word)

    counts = dict()
    for rows in db:
        counts[rows] = counts.get(rows,0) + 1

max_count = None
max_word = None
for word, count in counts.items():
    if max_count is None or count > max_count:
        max_count = count
        max_word = word
print(max_word,max_count)