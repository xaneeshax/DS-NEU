import pandas as pd

characters = pd.DataFrame({'characters' : ['Spongebob', 'Patrick', 'Squidward', 'Sandy'],
                           'home' : ['Pineapple', 'Rock', 'Building', 'Air Dome']})
print(characters, end = '\n\n')

patty_food = pd.DataFrame({'characters' : ['Spongebob', 'Mr.Krabbs', 'Squidward', 'Plankton'],
                           'occupation' : ['Cook', 'Manager', 'Cashier', 'Manager']})
print(patty_food, end = '\n\n')

# Returns the intersection of both of these data frames
# Known as Inner Merge
merged = pd.merge(characters, patty_food, on = 'characters')
print(merged, end = '\n\n')

# Returns the entirety of the data in the two dataframes
# Known as Full Join
merged = pd.merge(characters, patty_food, on = 'characters', how = 'outer')
print(merged, end = '\n\n')

# Returns the entirety of the data in the first dataframe and the rows that intersect
# Known as Left Join (Dataframe #1 + Innermerge)
merged = pd.merge(characters, patty_food, on = 'characters', how = 'left')
print(merged, end = '\n\n')

# Returns the entirety of the data in the second dataframe and the rows that intersect
# Known as Right Join (Dataframe #2 + Innermerge)
merged = pd.merge(characters, patty_food, on = 'characters', how = 'right')
print(merged, end = '\n\n')

# Use this notation when the column names are not the same
characters.rename(columns = {'characters' : 'doodles'}, inplace = True)
merged = pd.merge(characters, patty_food, left_index = True, right_index = True)
print(merged, end = '\n\n')

# Use this notation when one has no index and one does
characters.rename(columns = {'doodles' : 'characters'}, inplace = True)
characters.set_index('characters', inplace = True)
print(characters, end = '\n\n')
print(patty_food, end = '\n\n')
merged = pd.merge(characters, patty_food, left_index = True , right_on = 'characters', how = 'outer')
print(merged)
