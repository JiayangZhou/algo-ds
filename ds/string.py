# basic operations

s1 = "a"
_ = ord(s1) # a 97 A 65
print(_)
print(chr(_))

s1 = "abc"
s2 = "acb"
# compare two string lexicographically
print(s1 > s2)

print("s2[0]: " + s2[0])

s2 = "abcdef"
print(s2[1:10]) #bcdef
print(s2[1:3]) #bc
print(s2[:3]) #abc
print(s2[3:]) #def
print(s2[3:3] == "")

s = "0123456789123"
print(s[0:10])

s3 = "Abc"
s3.startswith("a")
s3.isdigit() # 1 2 3 
print("-1".lstrip("-").isdigit()) # remove "-" from front of the string
s3.isalpha() # "a" "b" "c"
s3.isalnum() # 1 2 3 "a" "b" "c"
s3.isupper()
s3 = s3.replace("a", " ").replace("b", " ").lower()
print(s3)

my_str = "   text "
my_str = my_str.strip()
my_str = "---text-"
my_str = my_str.strip("-") # remove "-" from front of the string and back of the string

a = "A"
print(a.lower())
print(a.upper())

s4 = "a"
ba = s4.upper()
ba = chr(ord(s4) - 32)
print(ba)

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
s_reversed = s[::-1] # cba, and time complexity is O(n)


# conversion
s = "abc"
a = list(s) # split string to char list ['a', 'b', 'c'] 
a = [*s] # split string to char list ['a', 'b', 'c'] 

l = ["a","b","cd"]
s = "".join(l)  # convert list to string
print(s)

s = "a b c d e"
l = s.split(" ")
print(l)
print("a b c".split()) # ['a', 'b', 'c'],  default is white space
print("abc".split()) # ['abc'],  default is white space

s="abcd"
print(set(s)) # same as this set([*cur])

# iteration 
s = "abc"
for i, c in enumerate(s):
   print(i, c)

s = "abcde"
for i in range(len(s)):
    print(i)
    # you cannot manipulate i as for is just looping <class 'range'>
    # print(type(range(len(s))))
# do something like this instead if you want to manipulate i
print(len(s[:0]))
s = "bxo#j##tw"
i = 0
while i < len(s):
    if s[i] == "#":
        s = s[:max(i - 1, 0)] + s[i + 1:]
        i = len(s[:max(i - 1, 0)]) - 1
    i += 1
print(s)

# sorting
s = ["a", "ab", "abc"]
s.sort(key=len, reverse=True)
print(s)

a = "cba"
b = "cab"
print(sorted(a))
print(sorted(a) == sorted(b))

a = "abc"
a += "z" # a = a + "z"
print(a)

a = ""
print(a[:-1] == "")

# find index of first 'bc' in string "abc"
index = "abc".index('bc')
print(index)

a = "abc"
print(a[:0]) # ""
print(a[:-1]) # ab
print(a[0:]) # abc

print(len("\\")) # the result is 1