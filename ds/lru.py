# https://leetcode.com/problems/lru-cache/
# use dictatory (map) and a deque (list)
class LRUCache:
    from collections import OrderedDict
    from heapq import heapify, heappush, heappop
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.d = dict()

    def get(self, key: int) -> int:
        if key in self.d.keys():
            self.queue.remove(key)
            self.queue.append(key)
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d.keys():
            self.queue.remove(key)
            self.queue.append(key)
            self.d[key] = value
        elif len(self.queue) < self.capacity:
            self.queue.append(key)
            self.d[key] = value
        else:
            temp = self.queue.pop(0)
            self.d.pop(temp)
            self.queue.append(key)
            self.d[key] = value
            
# use OrderedDict
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.d.keys():
            _ = self.d[key]
            self.d.pop(key)
            self.d[key] = _
            return _
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d.keys():
            self.d.pop(key)
            self.d[key] = value
        elif len(self.d) < self.capacity:
            self.d[key] = value
        else:
            self.d.popitem(0)
            self.d[key] = value