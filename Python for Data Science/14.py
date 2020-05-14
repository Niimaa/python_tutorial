import numpy as np
import matplotlib.pyplot as plt

a = [[11,12,13],[21,22,23],[31,32,33]]
A = np.array(a)

print(A)

print(A.ndim)
print(A.size)

print(A.shape)

print(A[1][2])
B = A[0,0:2]
print(B)

x=[[1,0],[0,1]]
X = np.array(x)
y = [[2,1],[1,2]]
Y = np.array(y)
z = X+Y
print(z)

f = 2*Y
print(f)

#element-wise or Hadamard product
g = X*Y;
print(g)

A = np.array([[0,1,1],[1,0,1]])
B = np.array([[1,1],[1,1],[-1,1]])
C = np.dot(A,B);
print(C)

X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]])
Z=np.dot(X,Y)
print(Z)


