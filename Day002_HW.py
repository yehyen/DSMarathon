import numpy as np

print(np)
print(np.__version__)

# Q1
a = np.random.randint(10, size=6)
print("type(a): ", type(a))
print("a.dtype", a.dtype)


# Q2 
def is_dtype(a, t):
    return a.dtype is t

print(is_dtype(a, 'int'))
print(is_dtype(a, np.int))
print(is_dtype(a, np.dtype("int")))

# Q3
# 第三


# Extanded
array1 = np.array(range(30))
# Q1
array = array1.reshape((5, 6)).ravel(order="F")
print(array)