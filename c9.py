import numpy as np

# Joining
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(np.concatenate((array1, array2)))

# Joining using axis
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

print(np.concatenate((array1, array2), axis=1))

# Stacking
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(np.stack((array1, array2), axis=1))

# Stacking along Rows
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(np.hstack((array1, array2)))

# Stacking along Columns
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(np.vstack((array1, array2)))

# Stacking along Height (depth)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(np.dstack((array1, array2)))