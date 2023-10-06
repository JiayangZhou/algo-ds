# basic operations
d = {}
d = dict()

a = d.setdefault("a", 1) # returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value
print(a)
print(d)

d = {"a": 1, "b": 2, "c": 3}
for k, v in d.items():
	print(k, v)

x = d.get("d", 4) # returns the value of the item with the specified key.
# If the  key does not exist, return the specified value 
print(x)

# creation 
from collections import defaultdict
d = defaultdict(list)
d = defaultdict(lambda: 1)

d = {_:set() for _ in range(0, 10)}

# deletion
d = {"a": 1, "b": 2, "c": 3}
print(d.pop("a"))
print(d.pop("a", 1))

del d["c"] # in place deletion, raise exception if not exist

# sort
d = {"a": 3, "b": 2, "c": 1}
print(d.items())

print(dict(sorted(d.items(), key=lambda x: x[1])))

