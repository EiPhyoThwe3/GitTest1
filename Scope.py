# # def scope_test():
# # 	def do_local():
# # 		spam = "local spam"

# # 	def do_nonlocal():
# # 		nonlocal spam
# # 		spam = "nonlocal spam"

# # 	def do_global():
# # 		global spam
# # 		spam = "global spam"

# # 	spam = "test spam"
# # 	do_local()
# # 	print("After local assignment:", spam)
# # 	do_nonlocal()
# # 	print("After nonlocal assignment:", spam)
# # 	do_global()
# # 	print("After global assignment:", spam)

# # scope_test()
# # print("In global scope:", spam)

# # def say_hello():
# # 	print('Hello World')

# # say_hello()

# #function parameter

# # a = input('Please enter A value: ')
# # b = input('Please enter B value: ')


# # def print_max(a, b):
# # 	if a > b:
# # 		print(a, 'is maximum')

# # 	elif a == b:
# # 		print(a, 'is equal to'.b)

# # 	else:
# # 		print(b, 'is maximum')


# # print_max(a, b)


# # print(20>10)
# # print(20 == 10)
# # print(20 < 10)
# # print(bool("Hello World"))
# # print(bool(20))

# # python Conditions

# # Equals 						-> x == y
# # Not Equals					-> x != y
# # Less than 					-> x <  y
# # Less than or equal to		-> x <= y
# # Greater than 				-> x >  y
# # Greater than or equal to 	-> x >= y


# # Local variables
# ------------------------------------------------------------
# def func(x):
# 	print('x is ', x)
# 	x = 2
# 	print('Changed local x to ', x)
# x = 10
# func(x)
# print('x is still', x)

# def func(y):
# 	print('y is ', y)
# 	y = 50
# 	print('Changed local y to ', y)

# def funx(y):
# 	print('y is ', y)
# 	y = x + y

# 	print('Y is changed to x + y', y)

# x = 40
# y = 20
# func(y)
# funx(y)
# print('y is still ', y)

# ------------------------------------------------------------

#Global Statement

# def func():
# 	global x

# 	print('x is ', x)
# 	x = 2
# 	print('Changed global x to ', x)

# x = 50
# func()
# print('Value of x is :', x)

# ------------------------------------------------------------


#eg.

# def func():
# 	global y
# 	print('y is ', y)

# 	y = 100
# 	print('value changed to ', y)

# y = 50
# func()
# print('value of y ', y)

# ------------------------------------------------------------
#eg.
# def do_global():
# 	global spam
# 	spam = "global spam"

# spam = "test spam"
# do_global()
# print("After global assignment: ", spam)

# ------------------------------------------------------------
#eg.

# def func():
# 	nonlocal x
# 	print('x is ', x)

# 	x = 5
# 	print('value of x is ', x)

# x = 10
# func()
# print("Real value of x is ", x) 

# ------------------------------------------------------------

#eg.

# def do_nonlocal():
# 	global spam
# 	spam = "global spam"
# 	nonlocal spam
# 	spam = "nonlocal spam"

# spam = "test spam"
# do_nonlocal()
# print("After nonlocal assignment : ", spam)


#testing
def scope_test():
	def do_local():
		spam = "local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"


	spam = "test spam"
	do_local()
	print("After local assignment:", spam)
	do_nonlocal()
	print("After nonlocal assignment:", spam)

scope_test()

