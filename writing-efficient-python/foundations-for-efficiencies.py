# ---------------------------------------- Efficient Python Code Definition ----------------------------------------
# writing efficient Python code:
# - minimal completion time (fast runtime)
# - minimal resource consumption (small memory footprint)

# example non-pythonic vs pythonic ----------------------------------------
numbers = [9,5,2,4,8,7]

# Non-Pythonic
doubled_numbers = []

for i in range(len(numbers)):
    doubled_numbers.append(numbers[i] * 2)

# Pythonic
doubled_numbers = [x * 2 for x in numbers]

# ---------------------------------------- Python Built-in ----------------------------------------
# Built-in types: list, tuple, set, dict, etc
# Built-in functions: print(), len(), range(), round(), enumerate(), map(), zip(), etc
# Built-in modules: os, sys, itertools, collections, math, etc

# ---------------------------------------- RANGE() FUNCTION ----------------------------------------
# range() parameters = range(start, stop, step)

# example range() function ----------------------------------------
even_nums = range(2, 11, 2)

even_nums_list = list(even_nums)
print(f'range() function : {even_nums_list}')

# example unpacking range() function ----------------------------------------
nums_list = [*range(1,12,2)]
print(f'create new list by unpacking a range object: {nums_list}')

# ---------------------------------------- ENUMERATE() FUNCTION ----------------------------------------
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# example enumerate() using for loop ----------------------------------------
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(f'enumerate() using for loop: {indexed_names}')

# example enumerate() using list comprehension ----------------------------------------
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(f'enumerate() using list comprehension: {indexed_names_comp}')

# example unpacking enumerate() ----------------------------------------
indexed_names_unpack = [*enumerate(names, start=1)]
print(f'unpacking enumerate() using *: {indexed_names_unpack}')

# ---------------------------------------- MAP() FUNCTION ----------------------------------------
# map() = applies a function over an object

# example map() function ----------------------------------------
nums = [1.5, 2.3, 3.4, 4.6, 5.0]

rnd_nums = map(round, nums)

print(f'map() function: {list(rnd_nums)}')

# example map() with lambda (anonymous function) ----------------------------------------
nums = [1, 2, 3, 4, 5]

sqrd_nums = map(lambda x: x ** 2, nums)

print(f'map() function with lambda: {list(sqrd_nums)}')

# example unpacking map() function ----------------------------------------
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Unpack names_map into a list
names_uppercase = [*names_map]

print(f'unpacking to list from map() function {names_uppercase}')

# ---------------------------------------- NUMPY ARRAY ----------------------------------------
# Why using numpy array?
# - fast & memory efficient, alternative to Python lists
# - numpy array is homogeneous: only contains elements of the same type - this is why numpy array is memory efficient

# example python list vs numpy array ----------------------------------------
# python list
nums_list = list(range(8))
print(f'range() function using python list: {nums_list}')

# numpy array
import numpy as np

nums_np = np.array(range(8))
nums_np_list = [*nums_np]
print(f'range() function using numpy array: {nums_np_list}')

# example broadcasting ----------------------------------------
nums = [1, 2, 3, 4, 5]

# python list using for loop (inefficient option)
sqrd_nums_python_list = []
for num in nums:
    sqrd_nums_python_list.append(num ** 2)
print(f'broadcasting using python list: {sqrd_nums_python_list}')

# list comprehension (better option but not best)
sqrd_nums_list_comprehension = [num ** 2 for num in nums]
print(f'broadcasting using list comprehension: {sqrd_nums_list_comprehension}')

# numpy array (best solution)
import numpy as np

nums_np = np.array(nums)
nums_np_pow = nums_np ** 2
nums_np_list = [*nums_np_pow]
print(f'broadcasting using numpy array: {nums_np_list}')

# example 2D Indexing ----------------------------------------
# 2-D list (inefficient option)
nums2 = [[1, 2, 3],
        [4, 5, 6]]

# print row = 1, column = 2 using python list
first_row_second_column_list = nums2[0][1]
print(f'2D indexing list #1: {first_row_second_column_list}')

# print all of 1st row using python list
first_row_list = [row[0] for row in nums2]
print(f'2D indexing list #2: {first_row_list}')

# 2-D numpy array (best solution)
import numpy as np

nums2_np = np.array(nums2)

# print row = 1, column = 2 using numpy array
print(f'2D indexing numpy array #1:{nums2_np[0,1]}')

# print all of 1st row using numpy array
print(f'2D indexing numpy array #1:{nums2_np[:,0]}')

# example boolean indexing ----------------------------------------
nums = [-2, -1, 0, 1, 2]

# python list using for loop (inefficient option)
pos_for_loop_list = []
for num in nums:
    if num > 0:
        pos_for_loop_list.append(num)
print(f'boolean indexing using python list using for loop: {pos_for_loop_list}')

# list comprehension (better option but not best)
pos_list_comprehension = [x for x in nums if x > 0]
print(f'boolean indexing using python list comprehension: {pos_list_comprehension}')

# numpy array (best solution)
import numpy as np

nums_np = np.array(nums)

pos_numpy_array = nums_np[nums_np > 0]
print(f'boolean indexing using numpy array: {pos_numpy_array}')