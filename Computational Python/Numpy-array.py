import numpy as np

array1 = np.random.random((2,3))
print(array1)

array2 = np.random.random((2,3))
print(array2)

#Array Operations (Arrays should be in the same order)

array3 = array1 + array2
print(array3)

array4 = array1 - array2
print(array4)

array5 = array1*array2
array6 = array1/array2
print(array5)
print(array6)

array7 = np.arange(5)
print(array7)
array7 = array7 ** 2
print(array7)
#numoy array indexing
print(array7[:2])
array8 = np.arange(10)
print(array8[3:7])
array8[5] = 7
print(array8)
array8[5:]= 3
print(array8)
array9 = array8.copy()
print(array9)