# basic operations

# creation
a = [_ for _ in range(5) if _ > 2]
a = [_ if _ > 2 else 0 for _ in range(5)]
print(a)

a = [0] * 40
 
# n * n grid
import sys
n = 2
a = [[sys.maxsize] * n for _ in range(n)] 
print(a)