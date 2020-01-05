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


b = np.arange(12).reshape(3, 4)
b

b.sum(axis = 0)

b.min(axis = 1)

b.cumsum(axis = 1)


#Universal Functions

B = np.arange(3)
B

np.exp(B)
np.sqrt(B)

C = np.array([2., -1., 4.])
np.add(B, C)


a = np.arange(10)**3
a

a[2]
a[2:5]
a[6:2]
a
a[ : :-1]

for i in a:
	print(i**(1/3.))


#Multidimensional indices

def f(x, y):
	return 10*x+y

b = np.fromfunction(f, (5, 4), dtype=int)
b

b[2, 3]
b[0:5, 1]
b[ : , 1]
b[1:3, : ]

c = np.array( [[[  0,  1,  2],
				[ 10, 12, 13]],
               [[100,101,102],
                [110,112,113]]])
c.shape

c[1,...]
c[...,2]

for row in b:
    print(row)
for element in b.flat:
	print(element)

#Shape Manipulation
a = np.floor(10*np.random.random((3, 4)))
a

a.shape
