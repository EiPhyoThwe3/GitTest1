# x = int(input("Please enter an integer:"))
# 	#This is user input.

# if x < 0:
# 	x = 0
# 	print('Negative changed to zero')
# elif x == 0:
# 	print('zero')
# elif x == 1:
# 	print('Single')
# else:
# 	print('More')

# int - integer (Number)
# str - string (character)
# boolean - True , False
# float - 0.02, 0.5, 0.1

#comment

# x = int(input("Please enter an integer: "))

# if x < 5:
# 	print('X is smaller than 5.')
# elif x > 10:
# 	print('X is greater than 10.')
# elif x == 7:
# 	print('X is equal to 7.')
# elif x > 5 and x < 10:
# 	print('X is bigger than 5 and less than 10.')

# else:
# 	print('X is undefined.')



# x = int(input("Please enter an age: "))

# if x >= 1 and x <=18:
# 	print('Go to school')
# elif x >= 19 and x <= 50:
# 	print('Go to vacasion')
# elif x >= 51 and x <= 75:
# 	print('Go to temple')
# if x >= 76:
# 	print('Go to pagoda')

#print("I don't like it")

#Measure some strings:
# words = ['cat','windows','defenstrate']
# for w in words:
# 	print(w, len(w))

# fruits = ['apple', 'banana' , 'cucumber', 'pineapple', 'orange']
# for f in fruits:
# 	print(f, len(f))

for i in range(5):
	print(i)

for x in range(0, 10):
	print(x)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i, a[i])
#output
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb

# fruit = ['apple', 'banana', 'cucumber', 'pineapple', 'orange']
#  fruit.append('grape')
# 
# 
# fruit.append('grape')
# fruit
# ['apple', 'banana', 'cucumber', 'pineapple', 'orange', 'grape', 'grape']
# fruit.remove('grape')
# 
#  fruit
# ['apple', 'banana', 'cucumber', 'pineapple', 'orange', 'grape']
#  fruit.remove('grape')
#  fruit
# ['apple', 'banana', 'cucumber', 'pineapple', 'orange']
# 
# 
#  fruit = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#  fruit.count('apple')
# 2
#  fruit.count('tangerine')
# 0
#  fruit.index('banana')
# 3
#  fruit.index('banana',4)
# 6
#  fruit.reverse()
# 
#  fruit
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# fruit.append('grape')
#  fruit
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
#  fruit.sort()
# fruit
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
#  fruit.index('banana', 1)
# 2
# fruit.index('banana', 2)
# 2
#  fruit.index('banana', 3)
# 3