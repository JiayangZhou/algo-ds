from queue import PriorityQueue

pq = PriorityQueue() 

pq.put((2, 1, 3))
pq.put((1, 2, 3))
pq.put((3, 1, 2))

print(pq.get())
print(pq.qsize())
     
# priority queue is thread safe