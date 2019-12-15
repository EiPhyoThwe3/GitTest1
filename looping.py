#15.12.2019
#items()
knights = {'gallahad': 'the pure', 'robin': 'the brave', 'Hello': 'World'}
for k, v in knights.items():
	print(k, v)

for k in knights.items():
	print(k)

#enumerate()
for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

#zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#reversed()
for i in reversed(range(1, 10, 3)):
	print(i)
	

#sorted()
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
	print(f)

string1, string2, string3 = '', '', '3'
num = string1 or string2 or string3
num