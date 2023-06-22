"""
Numeric competing library
In python numeric processing is very slow so Python is not the right tool for solving that complex numbers. NumPy is actually solving
that, NumPy is very efficient numeric processing library that sits on top of Python.It's going to be using high performance numeric computations and arrays
representations etc.
"""

import sys
import numpy as np

# a = np.array([1,2,3,4])
# b = np.array([4,5,7,2.6])
# #print(a[0:]) #Starting at index 0(index 0 include) iterate all indexes [1,2,3,4]

# #print(a[1:3]) # [2,3]

# print(a[:])


#Broadcasting and Vectorized operations

# a = np.arange(4) #create a array that 4 value like 0,1,2,3

# result = a + 10 # 10,11,12,13

# result = a * 10 # 0 , 10 , 20 ,30

# result = a + 100 # 100, 101 ,102 ,103

# #l = [0,1,2,3] i *10 for i in l saves us to do this 

# print(result)


# Linear Algebra


# A = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# B = np.array([
#     [6,5],
#     [4,3],
#     [2,1]
# ])

# #print(A.dot(B)) # dot product


# print(B.T) #transp product



#Useful Numpy functions

# np.random.random(size=2)
# np.random.normal(size=2)

# np.arange(10).reshape(2,5)