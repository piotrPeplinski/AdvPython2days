import numpy as np
import time
from math import sqrt

array1 = np.array([[1,2,3], [4,5,6]])
array2 = np.array([[1,1,1], [2,2,2]])
#print('array2: ', array2)

array = np.array([-2,-1,0,2,3,4])
print(array)

def get_square_root(x):
    if x>0:
        return sqrt(x)
    else:
        return x

vectorized_sqrt = np.vectorize(get_square_root)

array = vectorized_sqrt(array)

print(array)
#numbers = numbers + 10

#array1 = array1 + 10

# #FOR LOOP
# start = time.time()

# numbers = [1,2,3,4,5]

# for index in range(len(numbers)):
#     numbers[index] += 10

# end = time.time()
# result_loop = end-start
# print('For loop: ', result_loop)

# #NUMPY ARRAY
# start = time.time()

# numbers = np.array([1,2,3,4,5])

# numbers +=10

# end = time.time()

# result_vector = end-start
# print('Vectorization: ', result_vector)

# print(f'Vectorization was quicker {round(result_loop/result_vector,2)} times')