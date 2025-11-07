import numpy as np

# Searching Arrays
array = np.array([1, 3, 2, 3, 2, 3, 4, 5, 3, 6])
print(f"Searching Arrays: {np.where(array == 3)}")

# Search Sorted
array = np.array([1, 6, 1, 3, 4, 5])
print(f"Search Sorted: {np.searchsorted(array, 6)}")