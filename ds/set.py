# basic operations
set1 = {"apple", "banana", "cherry", "Java"}

set1.add(32)
set1.discard("Java") # preferred over set1.remove("Java"), no exception raised
print(set1)

# clean
set1.clear() 
set1 = set()

# combine two sets
set1 = {1,2,3}
set2 = {4,5,6}

set_union = set1.union(set2)
set_union = set2.union(set1) # return a new combined set, or set3 = set1 | set2
set1.update(set2) # add set2 to set1
print(set_union)
print(set1)
print(set2)

# find intersection of two set
set1 = {1,2,3,4}
set2 = {4,5,6}

set3 = set1 & set2 # set3 = set1.intersection(set2)
print(set3) 

# subtraction 
set1 = {1,2,3,4}
set2 = {4,5,6}

set3 = set1 - set2 # set3 = set1.difference(set2), order matters
print(set3) 

# symmetric_difference
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

set3 = set()
for s in set1:
    if s not in set2:
        set3.add(s)
for s in set2:
    if s not in set1:
        set3.add(s)
print(set3)

set3 = set2 ^ set1 # set3 = set1.symmetric_difference(set2)
print(set3)

# addition
set1 = set()
set1.add((1,2)) # tuple is okay, but list is not hashable
