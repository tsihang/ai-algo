
## List
The best way to imagine a list in Python is as a horizontal bookshelf with elements inside it.
For example, consider a list of numbers such as 50, 30, 400, 11, 7, 24, 681, and so on.
This resembles a horizontal bookshelf containing these elements.

Lists in Python are similar to arrays in other programming languages such as C or C++. 

If you have studied these languages, you might be familiar with the concept of arrays.

In Python, lists are a separate concept, and we will discuss arrays later. For now, you
can think of a list as essentially an array or, if you have studied R programming, as a vector.

### Ordered Sequence and Indexing
```bash
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
```
This expression, `letters[0]`, returns the first element, which is *a*. Similarly, *letters[1]* returns *b*,
*letters[2]* returns *c*, and so forth.

### Determining the Number of Elements in a List
```bash
len(letters)
```

Since the list has five elements, *len(letters)* returns *5*. However, because list indices start at *0*,
 the last element's index is always *len(letters) - 1*. Therefore, to access the last element, you use *letters[4]*.

### Negative Indexing in Lists
```bash
letters[-1]
```

Another way to access elements is through *negative indexing*. In Python, the last element of a list
 has the index *-1*, the second last is *-2*, and so on. Note that there is no *-0* index.

### Overwriting List Elements
```bash
letters[2] = 63
```
You can overwrite values in a list by assigning a new value to a specific index. For example,
to change the element at index 2 to 63.

### Printing List
```bash
print(letters)
```
Now, if you print the list *letters*, you will see that the third element has been replaced with 63.

### range() function

The `range()` function is commonly used in for loops to generate a range of numbers to
iterate over. For example, `range(15)` creates a range object representing numbers from 0
up to, but not including, 15.

Using *range()* is convenient for generating sequences of numbers instead of typing them out manually.
For example, you can create a list of numbers from 0 to 7 by calling `list(range(8))`.

You can also specify a starting point other than zero. For example, `list(range(1, 8))` generates
 numbers from 1 up to, but not including, 8.

The range() function also accepts a third parameter: the step size. By default, the step is 1,
 meaning the sequence increments by 1 each time. You can specify a different step to generate
  sequences with different intervals. For example, `list(range(100, 111, 2))` generates even
  numbers between 100 and 110 inclusive. Similarly, `list(range(100, 201, 10))` generates numbers
   from 100 to 200 in steps of 10.

### Slicing in List
`:`
1. Slicing with Start and Stop Indices

`letters[:]`, full slicing, which returns the entire list.

`letters[2:]`, which slice from index 2 to the end.

`letters[:4]`, which slice from the beginning up to, but not including, index 4.

`letters[2:4]`, which extract elements from index 2 up to, but not including, index 4.

2. Advanced Slicing with Steps

`letters[1:4:2]`, which select every second element between indices 2 and 4.

`letters[::3]`, which select every third element.

3. Slicing with Negative Indices
`letters[-8:7]` and `letters[-8:-3]` show same result using negative indices.

4. Advanced Slicing with Negative Steps

`letters[::-1]`, which reverse the list.

### Mixed Types in Lists
```bash
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 1]
```

## Array
The main difference is that arrays require all elements to be of the same data type,
 unlike lists which can contain mixed types.

```bash
import numpy as np
letters = np.array([12, 455, 60, 63.3, True, 'ABC'])
```
If we print *letters*, we will see that all elements have been converted to `strings`
 because the array must have a uniform data type.


### Slicing in Array

Consider the array A. If we slice it as A[2:], we get all elements from index 2 onwards.
Alternatively, A[2:4] returns elements from index 2 up to but not including index 4. This
 is similar to list slicing.

However, an important distinction is that slicing arrays does not create a copy of the array.
Unlike lists, where slicing creates a new list with those values, array slicing creates a
 view of the original array.

For example, if we assign B = A[2:4], B is not a new array but a view of A. If we modify
 elements in B, the corresponding elements in A will also change.

## Tuple
*Tuples* are immutable sequences of values. They are similar to *lists* but cannot be changed
 after creation. Their contents remain constant throughout their lifetime.

```bash
letters= ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
```
You can access elements of a tuple using indices just like a list.

The immutability of tuples is useful when you want to ensure that data passed to functions
 or shared between objects remains constant and unmodified.

### Mixed Types in Tuples
```bash
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 1)
```

## Sets
Sets, are mutable, unordered sequences of unique elements. In fact, a set is a lot like a mathematical set because it doesn’t hold duplicate values.

```bash
letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
```

## Dictionaries
A dictionary in Python holds `key-value` pairs, but you’re not allowed to use an unhashable item as a key. The primary difference between a dictionary and a set is the fact that it holds *key-value* pairs instead of single values.

```bash
letters = {'a': 1, 'b'：2, 'c'：3, 'd'：4, 'e'：5, 'f'：6, 'g'：7, 'h'：8, 'i'：9, 'j'：10}
```
### Mixed Types in Tuples

```bash
letters = {'a': 1, 'b'：2, 'c'：3, 'd'：4, 'e'：5, 'f'：6, 'g'：7, 'h'：8, 'i'：9, 'j'：10, 'l': true}
```
Dictionaries can store values of different types, just like lists in Python.

## Strings




## Reference

https://www.udemy.com/course/python-coding/