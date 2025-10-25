import numpy as np

array = np.array([1, 2, 3, 4, 5])

print(f"[start:end]: {array[2:5]}")
print(f"[start:]: {array[3:]}")
print(f"[:end]: {array[:4]}")

print(f"Negative slicing: {array[-5:-1]}")

print(f"[start:end:step]: {array[2:5:2]}")
print(f"[::step]: {array[::2]}")

two_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(f"Slicing 2-D arrays: {two_array[1, 2:5]}")