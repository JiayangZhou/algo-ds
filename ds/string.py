# basic operations

s1 = "a"
_ = ord(s1) # 97
print(_)
print(chr(_))

s2 = "abc"
print(s2[1:10]) #bc

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