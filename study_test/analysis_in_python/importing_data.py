#  importing a text file
with open('file_name', 'r') as file:
    print(file.read())

# importing csv
import pandas as pd
df = pd.read_csv('file_name')
df.head()

# importing pickled file
with open('file_name.pkl', 'rb') as file:
    d = file.load(file)
print(d)

# importing from database
from sqlalchemy import create_engine

# import data from internet
from urllib.request import Request, urlopen

# extract-table-from-web with pandas
pd.read_html('web-link')

