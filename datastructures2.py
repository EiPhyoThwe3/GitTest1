#24. 11. 2019

# The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a

del a[2:4]
a

del a[:]

t = 12345, 54321, 'hello!'
t[0]
t[:]

t = 1, (2, 3, 4, 5, 6, 7, 8 , 9, 10)
u = t, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
u

v = ([1, 2, 3], [4, 5, 6])
x = ([7, 8, 9], [0, 1, 2])
z = v + x
z
z[0]

empty = ()
len(empty)

singleton = 'hello',
len(singleton)

 basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
 print(basket)

b = {'banana', 'apple', 'cucumber', 'pineapple', 'orange', 'grape', 'apple', 'banana'}

print(b)

print(b)
'orange' in b

'grass' in b

a = set('mgmgmamamyamyaayeaye')
a 		# unique letters in a

b = set('kokoaungaungkyikyikyukyu')
b

c = set('1234567890')
c

a - b 		# letters in a but not in b
a | b 		# letters in a or b or both
a & b 		# letters in both a & b
a ^ b 		# letters in a or b but in both

b - a
b | a
b & a
b ^ a

c - b - a

a = {x for x in 'mgmgmamamyamyaayeaye' if x not in 'agye'}
a