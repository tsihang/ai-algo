import numpy as np

# String
s = "Hello" + " " + "World"
print(s)

# Integer
a = 10
b = 20
c = a + b
print(c)

# Float
d = a / b
print(d)

# list
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(list)

# Negative indexing in Lists
print(list[-1])

# Slicing.
print(list[:])
print(list[:4])
print(list[4:])
## The expression will extract elements in list from index 2 up to,
## but not including, index 4.
print(list[2:4])
## Negative slicing
print(list[-8:7])
print(list[-8:-3])

## Reverse the list
print(list[::-1])

# Advanced slicing with step
# The expression will select every second element between indices 2 and 5
print(list[1:5:2])

# Mixed type in list.
# Modify last elements to 12, an integer.
list[-1] = 12

# Array
# Convert the list to array.
array = np.array(list)
print(array)
## Slicing in array
## if we assign array_b = array[2:4], array_b is not a new array but
## a view of array. If we modify elements in array_b, the corresponding
## elements in array will also change.
array_b = array[2:4]
print(array_b)
array_b[0] = 'x'
print(array)

# Tuple
## Tuples are immutable sequences of values. They are similar to list but cannot be changed
## after creation. 
tuple= ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(tuple)
print(tuple[1:5:2])
print(tuple[::-1])

# Set
## 'set' object is not subscriptable
set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
print(set)

# Dictionaries
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
print(dict)
print(dict['a'])
print(len(dict))