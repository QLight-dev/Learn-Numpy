import numpy as np
import random # To generate random numbers 

# Filtering Arrays
array = np.array([65, 66, 67, 68, 69])
filter_array = [True, False, True, False, True] 
print(f"Filtering Arrays (T, F, T, F, T): {array[filter_array]}")

# Creating Filter Directly From Array
array = np.array([random.randint(0, 100) for _ in range(5)])
filter_array = array % 2 == 0
print(f"Array: {array}")
print(f"Filtered Array: {array[filter_array]}")