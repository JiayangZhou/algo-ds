from heapq import heappush, heappop, heapify

a = [5, 7, 9, 1, 3]
heapify(a) # time complexity is O(n)

heappush(a, 4)
s = heappop(a) # time complexity is O(log n)
print(s)

# not thread safe

# heap[0] is always the smallest element
print(a[0])

a.remove(3)
heapify(a) # after remove or pop, you need to heapify list again to heap 
print(a[0])

