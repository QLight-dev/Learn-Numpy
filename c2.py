import numpy as np

# accessing 1-D arrays

array = np.array([1, 2, 3, 4])

print(array[0])

print(array[1] + array[3])

# accessing 2-D arrays

two_array = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10]])

print(two_array[1, 4])

# accessing 3-D arrays

three_array = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 
               [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

print(three_array[1, 0, 2])

# negative indexing

print(three_array[-1, -1, -2])