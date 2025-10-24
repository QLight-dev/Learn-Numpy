import numpy as np

array = np.array([1, 2, 3, 4])
tuple_array = np.array((1, 2, 3, 4, 5))

print(array)
print(type(array))
print(tuple_array)
print(type(tuple_array))

# 0-D (scalar)
zero_array = np.array(69)
print(f"0D array:\n {zero_array}")
print(zero_array.ndim)

#1-D 
one_array = np.array([1, 2, 3])
print(f"1-D array:\n {one_array}")
print(one_array.ndim)

#2-D
two_array = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2-D array:\n {two_array}")
print(two_array.ndim)

#3-D
three_array = np.array([[[1, 2, 3], [4, 5, 6]], 
                        [[7, 8, 9], [10, 11, 12]]])
print(f"3-D array:\n {three_array}")
print(three_array.ndim)