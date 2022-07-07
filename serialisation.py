
import pickle

class myBio:
    def __init__(self, name, skill, field, potentials):
        self.name = name
        self.skill = skill
        self.field = field
        self.potentials = potentials

    def read_bio(self, additional):
        print(self.name)
        print(self.skill  + ', ' + additional)
        print(self.field)
        print(self.potentials)

myBio_object = myBio('Fewa', 'Python', 'Data Science', 'Problem solver')
myBio_object.read_bio('PostgreSQL')

# write to pickle
with open('myBio.pickle', 'wb') as file:  # it a binary, its not readable
    pickle.dump(myBio_object, file)

# read from pickle
with open('myBio_pickle', 'rb') as file:
    myBio_object = pickle.load(file)
    myBio_object.read_bio('PostgreSQL')





# serialising with json
import json

def add_bio(bio_json, name, salary):
    salaries = json.loads(bio_json)
    salaries[name] = salary

    return json.dumps(salaries)

# test code
salaries = "{'Bamb': 3000, 'Jark': 1400}"
new_salaries = add_bio(salaries, 'Me', 9000)
decoded_salaries = json.loads(new_salaries)
decoded_salaries

print(decoded_salaries['Bamb'])
print(decoded_salaries['Jark'])
print(decoded_salaries['Me'])



dir(json)





