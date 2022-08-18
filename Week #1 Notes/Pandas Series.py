import pandas as pd
import numpy as np

# List to Series
grades = np.array([87, 100, 91])
# Doesn't have to be numpy array
# grades = [87, 100, 91]
grades = pd.Series(grades, index = ['Harry', 'Hermione', 'Ron'])

print('List to Series')
print(grades)

# Dictionary to series
class_grades = {'Harry' : [87, 89], 'Hermione' : [100, 90], 'Ron' : [91, 90]}
class_grades = pd.Series(class_grades)

print('\nDictionary to Series')
print(class_grades)
print(class_grades[1], class_grades['Hermione'])

# Iterating through the Series
print('\nIterating through Series')

for grade in class_grades:
    print(grade)

for key in class_grades.keys():
    print(key)

for key, item in class_grades.iteritems():
    print(key, "got", item)
