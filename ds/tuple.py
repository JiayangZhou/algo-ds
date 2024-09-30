a = (1, 2) 
print(a[0])
# a[0] = 2 not working! tuple object does not support item assignment

a = [1, 2, 3, 4]
print(tuple(a)) # (1, 2, 3, 4)

a = ["a", "b", "c"]
print(tuple(a)) # ('a', 'b', 'c')