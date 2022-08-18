import pandas as pd

# Automatically assigns missing values with NaN
# Skips rows that have ALL NaN values
df = pd.read_csv('friends.csv', skip_blank_lines = True)
print(df, end = "\n\n")

# If there is a place holder for a missing value use:
# pd.read_csv(filename, na_values = "-99") OR
# df.replace(-99, 'NaN')
'''
    Other Replace Methods
'''

# df.replace([-99, -999], 'NaN')
# df.replace([-99, -999], ['NaN', 0])
# df.replace({-99 : 'NaN', -999 : 0})

# Drops all rows with missing values
df_clean = df.dropna()
df_clean.reset_index(inplace = True)
print(df_clean, end = "\n\n")

# Drop all rows that have ALL NaN
# df = df.dropna(how = 'all')

# Drop all colomns that have ALL NaN
# df = df.dropna(how = 'all', axis = 1)

# NOTE: Pandas automatically ignores missing values

# Assign values for Missing data
df_also_clean = df.fillna(0)
print(df_also_clean, end = "\n\n")

# Assign different values for missing data
default = {}
for header in list(df.columns):
    if header == 'rank' or header == 'salary':
        default[header] = 0
    elif header == 'age':
        default[header] = 30
    else:
        default[header] = ''
df_also_also_clean = df.fillna(default)
print(df_also_also_clean, end = "\n\n")

'''
    Duplicated Data Set
'''

# Add an index to the dataset
df = df.append(df.iloc[1])
print(df.duplicated(), end = "\n\n")

# Checks if the row has already been mentioned in the dataset
# and then drops the rows
df.drop_duplicates()

# Checks for duplicate values in those specific columns
# Only keeps the last such value in the dataframe
df.drop_duplicates(['salary'], keep = 'last', inplace = True)
print(df, end = "\n\n")

'''
    Apply & Map
'''

# Capitalize all the names on the column
df['name'] = df['name'].str.title()

# the Map method allows you to use a custom function
# on the dataset
# Maps the function to each item in the series object
def lword_only(career):
    return career.split()[-1]
df['career'] = df['career'].map(lword_only)

# The Apply Method changes the the series object across the
# an entire dataframe
# It is fairly similar to the Map method however it changes every value
# that applies to the function
def add_salary(salary):
    return salary + 5000
df['salary'] = df['salary'].apply(add_salary) 
print(df)

