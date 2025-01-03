# basic operations
d = {"a": 1, "b": 2, "c": 3}
for k, v in d.items():
	print(k, v)

x = d.get("d", 4) # returns the value of the item with the specified key.
# If the  key does not exist, return the specified value 
print(x)
print(len(d))

print("a" in d) # same as "a" in d.keys()

# creation 
d = {}
d = dict()
d = dict([("1", 1)])
d = dict({"1": 1})

from collections import defaultdict
d = defaultdict(list)
d = defaultdict(lambda: 1)

d = {_:set() for _ in range(0, 10)} # cannot use dict(xxx)

# addition
a = d.setdefault("a", 1) # returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value
print(a)

# deletion
d = {"a": 1, "b": 2, "c": 3}
print(d.pop("a")) # will raise error too if "a" not in d
print(d.pop("z", 404)) # will not raise error

del d["c"] # in place deletion, raise exception if not exist

# sort
d = {"a": 3, "b": 2, "c": 1}
print(d.items()) # dict_items([('a', 3), ('b', 2), ('c', 1)])
print(dict(sorted(d.items(), key=lambda x: x[1]))) # {'c': 1, 'b': 2, 'a': 3}
print(sorted(d.items(), key=lambda x: x[1])) # [('c', 1), ('b', 2), ('a', 3)]

from collections import OrderedDict
# OrderedDict maintains the order of insertion
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3 # Add a new item to the end of the dictionary
# od.popitem() # pop last insertion
od.popitem(0) # pop first insertion, 0 is the index
for key, value in od.items():
    print(key, value)

print(od.keys()) # odict_keys(['b', 'c'])
print(od.values()) # odict_values([2, 3])

