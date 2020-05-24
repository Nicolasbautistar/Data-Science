# -*- coding: utf-8 -*-
"""numpy_challenge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/juancasi/data_science_fundamentals/blob/master/chapter_04/numpy_challenge.ipynb

#NumPy Challenge

Create a NumPy ndarray object by using this list of numbers [7,8,4,5,1,2].
"""

import numpy as np

arr1 = np.array((7, 8, 4, 5, 1, 2))
print(arr1)

"""Using slicing print the elements from index 3 to the end of the array."""

print(arr1[3:])

"""Using slicing print all the elements except the last one."""

print(arr1[:-1])

"""Using slicing print the elements from index 1 to index 4 of the array."""

print(arr1[1:5])

"""Reshape the array into a 3 rows and 2 cols (3,2)."""

newarr = arr1.reshape(3, 2)
print(newarr)

"""Print all the array elements one by one (iterating)."""

for x in arr1:
  print (x)

"""Create a new NumPy ndarray object by using this list of numbers [0,6,9]."""

arr2= np.array((0,6,9))
print (arr2)

"""Join the two arrays."""

arr = np.concatenate((arr1, arr2))
print (arr)

"""Using filtering print only the odd numbers of the joined array."""

#Filter to select odd numbers
filter_arr = arr % 2 == 1

newarr = arr[filter_arr]
print(arr)
print(filter_arr)
print(newarr)

"""Sort the joined array elements."""

sortarr=(np.sort(arr))
print(sortarr)

"""Store in an array the names of the months."""

months=np.array(('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
print(months)

"""Split the months array in 4 periods of 3 elements each one."""

period = months.reshape(4, 3)
print (period)

"""Create an array with genre information ['F','M','F','F','M','F']."""

genre=np.array(('F','M','F','F','M','F'))
print(genre)

"""Find the indexes where the value is F."""

arregloF = np.where(genre=='F')

print(arregloF)

"""Store in an array the age information [18,20,19,23,19,20]."""

age=np.array((18,20,19,23,19,20))
print(age)

"""Create a filter array with values < 20."""

filter_arr = age < 20

newarr = age[filter_arr]

print(newarr)

"""Change the 3 index element with a value of 22"""

age=age.view()
age[3]=22
print(age)

"""Print the 4 index element."""

print(age[4])