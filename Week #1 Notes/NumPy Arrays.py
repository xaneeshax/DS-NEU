import numpy as np
'''
    Array Dimensions
'''
numbers = [[1, 10, 100, 1000], [2, 20, 200, 2000]]
print(numbers)

# Convert an list to a numpy array
# Note: the values do not have to be the same datatype
numbers = np.array(numbers)
print(numbers)

# Datatype of the array
print(numbers.dtype)

# Dimensions of an Array
print(numbers.ndim)

# Shape of the array
print(numbers.shape)

# Total Numbers in an Array
print(numbers.size)

# Dimensions of the array
print(len(numbers))

# Iterate by Rows
for item in numbers:
    for num in item:
        print(num)

# Iterate by Columns
for i in range(numbers.shape[1]):
    for j in range(numbers.shape[0]):
        print(numbers[j, i])

# Iterate by Rows
for number in numbers.flat:
    print(number, end = " ")

print()

'''
    Filling an Array
'''
# 5 x 1 Array of Zeros
# Floats
zeros = np.zeros(5)
print(zeros)

# Ints
zeros = np.zeros(5, dtype = 'int')
print(zeros)

# 2 x 4 Array of Ones
# Floats
ones = np.ones((2,4))
print(ones)

# 3 x 2 Array of 3000s
# Ints
full = np.full((3,2), 3000)
print(full)

# Arange for an array
print(np.arange(5))

# Arange for an array
print(np.arange(10, -1, -2))

# Shape and arange an array
cool = np.arange(1,31).reshape(5,6)
print(cool)
print(cool.sum())
print(cool.min())
print(cool.max())
print(cool.mean())
print(cool.var())


