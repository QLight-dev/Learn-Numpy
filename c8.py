import numpy as np

 # Iterating through all scalar elements in 1-D arrays
one_array = np.array([1, 2, 3])
print("All scalar elements in 1-D array: ")
for i in one_array:
    print(i)

# Iterating through all scalar elements in 2-D array
two_array = np.array([[1, 2, 3], [4, 5, 6]])
print("All scalar elements in 2-D array: ")
for x in two_array:
    for y in x:
        print(y)

# Iterating through all scalar elements in 3-D array
three_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("All scalar elements in 3-D array:")
for x in three_array:
    for y in x:
        for z in y:
            print(z)

# Iterating using nditer()
array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("All scalar elements using nditer(): ")
for i in np.nditer(array):
    print(i)