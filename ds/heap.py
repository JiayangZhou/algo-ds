from heapq import heappush, heappop, heapify

a = [5, 7, 9, 1, 3]
heapify(a)

heappush(a, 4)
s = heappop(a)
print(s)

# not thread safe

# heap[0] is always the smallest element
print(a[0])