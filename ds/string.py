# basic operations

s1 = "a"
_ = ord(s1) # 97
print(_)
print(chr(_))

s2 = "abcdef"
print(s2[1:10]) #bcdef
print(s2[1:3]) #bc
print(s2[:3]) #abc
print(s2[3:]) #def

# split string to half
s2 = "abcdef"
s2 = "abcdefg"
if len(s2) % 2 == 0:
    print(s2[:(len(s2) >> 1)]) # len(s2) >> 1 is 3 which is d
    print(s2[(len(s2) >> 1):])
else:
    print(s2[:(len(s2) >> 1)]) # len(s2) >> 1 is 3 which is also d
    print(s2[(len(s2) >> 1) + 1:])

s = "1212"
s.count("1")

# modification
s = "abc"
s_reversed = s[::-1] # cba


# conversion
s = "abc"
a = list(s) 
a = [*s] # split string to char list ['a', 'b', 'c'] 

l = ["a","b","cd"]
s = "".join(l)  # convert list to string
print(s)

# iteration 
s = "abc"
for i, c in enumerate(s):
   print(i, c)
