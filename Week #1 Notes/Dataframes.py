
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('precision', 2)


data = pd.read_csv('grades.csv', header = None)
data = data.rename(columns = {0 : 'Exam #1', 1 : 'Exam #2', 2 : 'Exam #3'})
data.index = ['Calculus', 'Accounting', 'Entreprenuership', 'Data Science']

# Access Rows
print(data['Exam #1'])
print(data.loc[['Calculus', 'Data Science'], :])
print(data.loc['Calculus':'Data Science', ['Exam #1', 'Exam #2']])

print(data.iloc[[0, 1, 3], 0])
print(data.iloc[0:2, 2:100])
# Does not work
# print(data[0])

print(data.at['Calculus', 'Exam #3'])
print(data.iat[0, 2])

      
# Row Average
print(data.mean())

# Access Columns
print(data.T.mean())

'''
df.reset_index(drop = False) -> will change the index column to
a regular column and setting drop to false ensures that the value
is still kept in the dataframe
'''

'''
Reading Files

pd.read_excel()
pd.to_excel()
df.to_csv()
reaed_html
read.json
'''
