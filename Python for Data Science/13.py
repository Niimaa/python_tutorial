#python list
a=["0",1,"two","3",4]
print(a)
print(a[0])
#numpy array (same size and same type)
import numpy as np
a = np.array([0,1,2,3,4])
print(a)
print(a.size)
print(a.ndim)
print(a.shape)
print(type(a))
#indexing and slicing
b=np.array([20,1,2,3, 4])
print(b)

b[4] = 100
print(b)
c=b[1:4]
print(c)
#vector addition and subtraction
#old style
u = [1,0]
v = [0,1]
z = []
for n,m in zip(u,v):
    z.append(n+m)
print(z)

#or use numpy
u = np.array([1,0])
v = np.array([0,1])
z = u+v
print(z)
x = u-v
print(x)
#Array multiplication

g = np.array([3,4])
h = 2 * g
print(h)
i = np.array([4,3])
h = g * i
print(h)
#DOT product
a = np.array([1,2])
b = np.array([3,1])
result = np.dot(a,b)
print(result)
#Adding constant to an numpy array
u = np.array([1,2,3,-1])
z = u + 1
print(z)

#universal function
#operates on ND array
a = np.array([1,-1,1,-1])
mean_a = a.mean()
print(mean_a )

b=np.array([1,-2,3,4,5])
max_b = b.max()
print(max_b)

print(np.pi)
x=np.array([0,np.pi/2,np.pi])
print(x)

y = np.sin(x)
print(y)

print(np.linspace(-2,2,num=5))
print(np.linspace(-2,2,num=9))
x = np.linspace(0,2*np.pi,100)
print(x)
y=np.sin(x)
print(y)
#plot the function
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()
