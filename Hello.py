# -*- coding: utf-8 -*-
print('Hello World!')
print('1024 * 768 =',1024*768)
print('''213
132
312
''')
print('\\\t\\')
print(r'\\\t\\')
print('中文')

user = ['JACK','DOLER','PICK','WOODER']
print(user)
print(user[0],user[-1])
print(len(user))
user.append('GITA')
print(user)
user.insert(2,'PUPPY')
print(user)
user.pop()
print(user)
user.pop(3)
print(user)
department = ('Finance','Research','Purchase','Test','Sale')
print(department)

L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]

print(L[0][0],L[1][1],L[2][2])