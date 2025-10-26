import numpy as np 

# Copy
array = np.array([1, 2, 3, 4, 5])
copied_array = array.copy()
array[0] = 67

print(f"Original Array: {array}")
print(f"Copied Array (Edited): {copied_array}")

# View
array = np.array([1, 2, 3, 4, 5])
viewed_array = array.view()
array[0] = 67

print(f"Original Array: {array}")
print(f"Viewed Array: {viewed_array}")

# Check if Array Owns its Data
print(f"Copied Array Base: {copied_array.base}")
print(f"Viewed Array Base: {viewed_array.base}")