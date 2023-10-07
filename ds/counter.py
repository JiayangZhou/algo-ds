from collections import Counter

s = "abc"
c = Counter(s)

print(c) # Counter({'a': 1, 'b': 1, 'c': 1})
print(c["a"])

c.update("a")
print(c)
c.update({'a':1, 'd':5})
print(c)

c["d"] = 2
print(c) 