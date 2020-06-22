import numpy as np
array1 = np.arange(100)
print(array1)
array1 = array1.reshape(10,10)
print(array1)
#first value is the row and second is the column
#print specific index in the 2d array
print(array1[1,3])
#reshape to 3 dimensional array
array1 = array1.reshape(5,4,5)
print(array1)
print(array1[0])
print(array1[0,1])
print(array1[0,1,2])

#array operations
array1 = np.arange(100)
array1 = array1.reshape(5,4,5)
print(array1)

array2 = np.arange(100)
array2 = array2.reshape(5,4,5)
print(array2)

array3 = np.add(array1,array2)
print(array3)

array4 = np.multiply(array1,array2)
print(array4)

array5 = np.subtract(array1,array2)
print(array5)

array6 = np.minimum(array1,array2)
print(array6)

#transpose of arrau
array7 = np.arange(10).reshape(2,5)
print(array7.transpose())

#statistic operations
print(array7.sum())
print(array7.mean())
print(array7.std())
print(array7.var())

#where statement for array
print(array7)
array8 = np.where(array7<=3,0,array7)
print(array8)


