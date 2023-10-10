import sys
import math

a = sys.maxsize
print(-a)

a = 1
b = 3
c = abs(a - b) 
print(c)

print(-float('inf') < 0)

# calculation
n = 9
print(int(math.sqrt(n)))

print(math.floor(3/2)) # print(10//2) # floor division
print(math.ceil(3/2))

print(5 >> 1)

# conversion
a = 10
a_bin = bin(a)
print(a_bin)
print(int(a_bin, 2)) 

# random
import random
r = random.randrange(0, 100) # return a number from 0 to n - 1
print(r)

r = random.randint(0, 10) # returns a random number from [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]