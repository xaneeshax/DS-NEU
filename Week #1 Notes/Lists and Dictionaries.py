'''
    Lists
'''
bowling = [60, 63, 70, 76, 82, 91, 98, 84, 85, 89]
# Reversing a List
print(bowling[::-1])

# Print alternate values starting from index 1
print(bowling[1::2])

# Use "continue" to halt a single code block
for i in range(len(bowling)):
    if i % 2 == 0:
        print(bowling[i])
    elif i == 7:
        continue
    else:
        print(bowling[i] * 2)

'''
    Dictionaries
'''

locations = {'San Francisco' : 'Fisherman\'s Wharf',
             'Los Angeles' : 'Walk of Fame',
             'New York' : 'Times Square', 'Seattle' : 'Mt. Ranier',
             'Boston' : 'Newberry Street', 'Las Vegas' : 'M&M Factory',
             'Washington D.C' : 'White House'}

# Convert values into a list
print(list(locations.values()))

# Convert keys into a list
print(list(locations.keys()))

# Get key-value pairs as tuples
print(list(locations.items()))

#Iterating through a dictionary
for city, place in locations.items():
    print("I visited {} in {}".format(place, city))

#Accessing and updating values
locations['New York'] = 'Empire State'

# Get the value of SF
print(locations.get('San Francisco'))

# Get a value for a key not in dictionary
print(locations.get('Portland', 'Not in locations'))


