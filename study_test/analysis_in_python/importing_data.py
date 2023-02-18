#  importing a text file
with open(file_name, 'r') as file:
    print(file.read())

# importing csv
import pandas as pd
df = pd.read_csv(file_name)
df.head()

# 