import numpy as np 

# S - string
string_array = np.array(["apple", "bananna", "ice cream"])
print(f"String: {string_array.dtype}")

# i - integer
int_array = np.array([1, 2, 3, 4, 5])
print(f"Int: {int_array.dtype}")

# Creating with Defined Data Type
data_array = np.array([1, 2, 3, 4, 5], dtype="i")
print(f"With Defined data type: {data_array}\ntype: {data_array.dtype}")

# Creating with Defined Size
size_array = np.array([1, 2, 3, 4], dtype="i4")
print(f"With Defined Size: {size_array}\ntype: {size_array.dtype}")

# Converting Data Types on Exsisting Arrays
original_array = np.array([True, False, True, False])
converted_array = original_array.astype('i')
print(f"original Array: {original_array} type: {original_array.dtype}\nNew Array: {converted_array} type: {converted_array.dtype}")
