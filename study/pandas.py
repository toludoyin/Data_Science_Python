
import pandas as pd

# create a dataframe
animals = ['cats', 'cattle', 'chicken', 'birds', 'cricket', 'dogs', 'ducks', 'humans', 'hyenas', 'lions', 'mosquitos', 'rats', 'tigers', 'whales', 'zebras']
sounds = ['mew', 'moo', 'cluck', 'twitter', 'creak', 'bark', 'quack', 'talk', 'laugh', 'roar', 'whine', 'squeak', 'growl', 'sing', 'whinny']
Digestion = ['ruminant', 'ruminant', 'ruminant','ruminant','ruminant','ruminant','ruminant','ruminant','ruminant','ruminant','ruminant','ruminant','ruminant','ruminant','ruminant']

dataframe = pd.DataFrame(list(zip(animals, sounds)), columns= ['animals', 'sounds'])
print(dataframe)

# [start:stop:step]