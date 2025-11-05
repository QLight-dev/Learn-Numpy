import numpy as np

# Splitting
array = np.array([1, 2, 3, 4, 5, 6])
print(f"Split Array: {np.array_split(array, 3)}")

# Splitting 2-D Arrays
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Splitting 2-D : {np.array_split(array, 4)}")

# Using hsplit()
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(f"Using hsplit(): {np.hsplit(array, 3)}")

# ...