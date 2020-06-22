import numpy as np
array1 = np.array([4,6,8,9])
print(array1)
array2 = np.arange(10)
print(array2)
print(array1)
array3 = array2.reshape(2,5)
print(array3)
print(array3.shape)
print(array3.dtype.name)
print(array3.ndim)
print(array3.size)

#Convert list to numpy array

months = ['Jan', 'Marc', 'Apr', 'jun']
month_array = np.array(months)
print(month_array)
print(months)
print(month_array.dtype.name)

months = ['Jan', 'Marc', 'Apr', 'jun', ['aug', 'sep', 'nov']]
print(months)

#creat zero array and unity array
array4 = np.zeros(100)
print(array4)
array4 = array4.reshape(10,10)
print(array4)

array5 = np.ones(100)
print(array5)
array4 = array5.reshape(10,10)
print(array5)

array6 = np.eye(6)
print(array6)
array6 = array6.reshape(6,3,2)
print(array6)

#empty and full array
array7 = np.empty((3,2))
print(array7)
array8 = np.full((3,2),1)
print(array8)