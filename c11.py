import numpy as np

# Searching Arrays
array = np.array([1, 3, 2, 3, 2, 3, 4, 5, 3, 6])
print(f"Searching Arrays: {np.where(array == 3)}")

# Search Sorted
array = np.array([1, 6, 1, 3, 4, 5])
print(f"Search Sorted: {np.searchsorted(array, 6)}")

# Search from the Right Side
array = np.array([2, 3, 4, 5])
print(f"Search from the Right Side: {np.searchsorted(array, 3, side="right")}")

# Search for multiple values
array = np.array([2, 4, 6, 8])
print(f"Search for multiple values: {np.searchsorted(array, [1, 3, 5, 7])}")

