from collections import Counter

s = "abc"
c = Counter(s) # possible also to create a counter c = Counter() first and update it

print(c) # Counter({'a': 1, 'b': 1, 'c': 1})
print(c["a"])

c.update("abc") 
print(c) # Counter({'a': 2, 'b': 2, 'c': 2})
c.update({'a':1, 'd':5})
print(c)

c["d"] = 2
print(c) 

c["d"] += 1
print(c)

a = [1, 2, 3, 3]
c = Counter(a)

c.pop(4, 0)
print(c.most_common())

print(c.items())

# example
# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring
def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    import collections
    count = collections.Counter()
    
    for i in range(len(s) - minSize + 1):
        t = s[i : i+minSize]
        if len(set(t)) <= maxLetters:
            count[t] += 1
    
    return max(count.values()) if count else 0