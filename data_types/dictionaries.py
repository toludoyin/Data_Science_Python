
dictionary_ = {'name': 'jam jam',
               'age': 100,
               'married': False,
               'job': 'data scientist'
               }

dictionary_['nationality'] = 'san-francisco' # add to dict
print(dictionary_)
print(dictionary_.get('age')) # to access a dict


key = ['no_1', 'no_2', 'no_3', 'no_4'] # convert lists to dict
values = [3, 10, 4, 7]

result = dict(zip(key, values))
print(result)

