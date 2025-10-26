import numpy as np 

# Reshaping from 1D to 2D

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
new_array = array.reshape(5, 3)

print(f"Old Array (1, 15): {array}")
print(f"Reshaped Array (5, 3): \n{new_array}")

# Reshaping from 1-D to 3-D
array = np.array([1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12,13, 14, 15])
new_array = array.reshape(1, 3, 5)

print(f"Old Array (1, 1, 15): {array}")
print(f"Reshaped Array (1, 3, 5): \n{new_array}")

# Unknown dimension
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
new_array = array.reshape(5, -1)

print(f"Old Array (1, 10): {array}")
print(f"With Unknown dimension Calculation: \n{new_array}")
print(f"Calculated Shape: {new_array.shape}")

# Flattening
array = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
new_array = array.reshape(-1)
print(f"Old Array (2, 2, 5): \n{array}")
print(f"With flattening (1, 20): {new_array}")