import numpy as np
a = np.arange(15).reshape(3, 5)
a

a.shape

a.ndim

a.dtype.name

a.itemsize

a.size

type(a)

b = np.array([6, 7, 8])
b

type(b)

#Array Creation

import numpy as np
a = np.array([2,3,4])
a

a.dtype

b = np.array([1.2, 3.5, 5.1])
b.dtype


np.zeros((3, 4))

np.ones((2, 3, 4), dtype = np.int16)

np.empty((3, 5))

np.arange(10, 30, 3)

np.arange(0, 2, 0.3)

np.linspace(0, 2, 9)


#Printing Arrays

a = np.arange(6)
print(a)

b = np.arange(12).reshape(4, 3)
print(b)

c = np.arange(24).reshape(2, 3, 4)
print(c)

print(np.arange(10000))
print(np.arange(10000).reshape(100, 100))

#Basic Operations

a = np.array( [20,30,40,50] )
b = np.arange( 4 )
b

c = a-b
c

b**2

10*np.sin(a)

a<35


A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

A * B

A @ B

A.dot(B)


a = np.ones((2, 3), dtype = int)
b = np.random.random((2, 3))

a *= 3
a

b += a
b

a += b


b = np.linspace(0,pi,3)
b.dtype.name

c = a+b
c

c.dtype.name

d = np.exp(c*1j)
d

d.dtype.name


a = np.random.random((2, 3))
a

a.sum()

a.min()

a.max()

