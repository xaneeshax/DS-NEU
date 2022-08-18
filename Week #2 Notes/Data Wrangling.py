import pandas as pd

# Add header = None when ther is no header in csv file
data = pd.read_csv('you.csv', header = None)

# Renames the columns
data = data.rename(columns = {0 : 'Name', 1 : 'First Season',
                              2 : 'Kills', 3 : 'Item'})
data = data.set_index('Name')
print(data, end = '\n\n')

# Gets the information by row
print(data.loc['Joe'], end = '\n\n')
print(data.loc['Paco'], end = '\n\n')
print(data.loc['Paco', 'Item'], end = '\n\n')

# Uses vector addition to add a new column
data['Score'] = data['First Season'] + data['Kills']

# Unique values in the column
# Returns a List
print(data['First Season'].unique())

#data = data.sort_index(ascending = False)

# axis = 0 is for the rows
# axis = 1 is for the columns
# ascending is reversing the direction it is ordered
data = data.sort_index(axis = 1, ascending = False)
print(data, end = '\n\n')

# You can list the data set using multiple factors
# Inplace means that the changes are assigned to the dataframe
# without having to equate the values to the data
# ex: data = data.somthing...
data.sort_values(by = ['First Season', 'Kills'], ascending = False, inplace = True)
print(data, end = '\n\n')

# Called Boolean Indexing
# Allows us to query a dataframe
# Is a series object
print(data['Kills'] > 1)

# THe where keyword argument is used for boolean indexing
dangerous = data.where(data['Kills'] >= 2)
print(dangerous, end = '\n\n')
dangerous.dropna(inplace = True)
print(dangerous, end = '\n\n')

# & to combine multiple conditions
# | to use a bitwise OR
dangerous = data[(data['Kills'] >= 2) & (data['First Season'] == 2)]
print(dangerous, end = '\n\n')

# Average for a column
print(data['Kills'].mean())

# Uses Boolean Indexing to keep the columns that we
# would like to keep using
columns_wanted = ['Kills', 'Item']
new_data = data[columns_wanted]
print(new_data)

print(data)

# Resets the column indexes so the names are 0,1,2...
data = data.reset_index()
print(data, end = '\n\n')

# Set the indexes of our dataframe using multiple attributes
# Generally make one over-arch the other
data = data.set_index(['First Season', 'Kills']).sort_index()
print(data, end = '\n\n')

# Returns all the indexes as tuples
# Will list all even if redundant - need to use 'unique' if
# you want the unique indices
print(data.index, end = '\n\n')

# You can select two indexes
print(data.loc[1, 0])

# You can also choose the first index and another column
print(data.loc[1, 'Score'].mean())


# You can select multiple rows using tuples
# Use the list notation otherwise you will get an error message
# from python
print(data.loc[[(1, 6), (2, 2)], ['Name']])





