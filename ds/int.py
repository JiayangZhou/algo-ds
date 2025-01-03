import sys
import math

a = sys.maxsize # float("inf") OR print(-math.inf)
print(-a)

print(max(1, 2, 3))
print(min(1, 2, 3))

a = 1
b = 3
c = abs(a - b) 
print(c)

print(-float('inf') < 0)
print(-float('-inf') < 0)

# calculation
n = 9
print(int(math.sqrt(n))) # same as n**0.5

print(math.floor(3/2)) # print(10//2) # floor division, rounding down 3.7 -> 3
# -3.7 -> -4
print(math.floor(-3/2)) # -2
# if you want to round towards 0 for negative and positive number
print(int(-3/2)) # -1 (removes the decimal portion without rounding)
print(int(3/2)) # 1, e.g. 3.7 -> 3 -3.7 -> -3

print(math.ceil(3/2)) # -(a//-b)
print(int(3.2)) # 3
print(round(2.23, 1))
print(5 >> 1)
#find the the greatest common divisor of the two integers
print (math.gcd(3, 6))
print (math.gcd(12, 6))
print (math.gcd(12, 36))

# conversion
a = 10
a_bin = bin(a)
print(a_bin) # 0b1010
print(int(a_bin, 2)) 

# random
import random
r = random.randrange(0, 100) # return a number from 0 to n - 1
print(r)

r = random.randint(0, 10) # returns a random number from [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]


# float number
nums1 = [1,3]
nums2 = [2]
nums = sorted(nums1 + nums2)
n = len(nums)
if n % 2 == 0:
    print(float((nums[n >> 1] + nums[(n >> 1) - 1]) / 2))
else:
    print(float((nums[n >> 1])))

a = 9
a = math.sqrt(a) # a is 3.0 and is float
a = 2
a **= 3 # a is 8
a = math.log(a, 2) # a is 3.0
a = 8
a = math.log2(a) # a is 3.0
a = 8
a = math.log(a) # if base is not specified, natural logarithm will be used (e)
# the change of base rule
print(math.log2(8))
print(math.log(8)/math.log(2))
print(math.log2(8) == math.log(8)/math.log(2))

print(math.pow(2, 3)) # 8.0
print(2 ** 3) # 8

y = 8  # Result
n = 3  # Exponent
x = y ** (1 / n) # Calculate the base
print(x)  # Output: 2.0

a = 0
target = {1, 2, 3}
a += 3 in target # only add 1 if that number is in target
print(a)

print(float(math.sqrt(9)) == int(3)) # you can compare float and int
print(type(float(math.sqrt(9))))
a = 4 / 2
print(a == 2)
print(type(a))