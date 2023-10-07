# basic operations
a = [1, 2, 3]
n = len(a)
total = sum(a)
print(total, n)

a = [1, 2, 3, 4, 3, 3]
count_3 = a.count(3)
print(count_3)

b = a.copy()  
print(b)

a = ['cat', 'dog', 'rabbit', 'horse']
index = a.index('dog') # returns the first index of the specified element

# creation
a = [_ for _ in range(5) if _ > 2]
a = [_ if _ > 2 else 0 for _ in range(5)]
print(a)

a = [0] * 40
print(a)

import sys
n = 2
a = [[sys.maxsize] * n for _ in range(n)] # n * n grid
print(a)

# modification
a.reverse() # reverse in place
a_reversed = list(reversed(a)) # return a reversed iterable object
print(a)
print(a_reversed)
print(a[::-1]) # return a reversed list

a = [1, 2, 3, 4]
b = a[:2] # [1, 2]
b = a[-2:] # [3, 4]

a = [1, 2, 3] + [4]
print(a)

# add same value to all element in a list 
a = [90,80,78,98,100]
b = [_ + 2 for _ in a if _ + 2 >= 0 ]
print(b)

# sort
a = [90,80,78,98,100]
a.sort() # sort in place
a = [90,80,78,98,100]
print(sorted(a))

a = [(1,3,1), (3,2,3), (2,1,2)]
a.sort(key=lambda x: x[0])
# a.sort(key=lambda x: x[0], reverse=True)
print(a)
print(sorted(a, key=lambda x: x[1]))
# print(sorted(a, key=lambda x: x[1], reverse=True))

a = [(1,3,1), (1,2,3), (2,2,2)]
print(sorted(a, key=lambda x: (x[1], x[0], x[2]))) # first criteria is x[1]
# second criteria is x[0], third criteria is x[2] 

from functools import cmp_to_key   
def comparator(x, y):
	return x[2] - y[2]
a.sort(key=cmp_to_key(comparator)) # sort with customized comparator
print(a)

# iteration 
s = [1, 2, 3]
for i, c in enumerate(s):
   print(i, c)
   
for i in range(1, 6, 2):
    print(i)