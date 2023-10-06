# deque
from collections import deque
dq = deque()
dq.append(4)
dq.append(5)
dq.appendleft(6) # 6, 4, 5
dq.pop()
dq.popleft() 

print(dq)

dq = deque([1,2,3,3,3])
if 5 in dq:
    dq.remove(5) # using remove() to remove the first occurrence of 3

print(dq)