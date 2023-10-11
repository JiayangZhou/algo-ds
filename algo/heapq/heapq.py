from heapq import heappush, heappop, heapify
from typing import List, Optional
# https://leetcode.com/problems/number-of-flowers-in-full-bloom
def fullBloomFlowers(flowers: List[List[int]], people: List[int]) -> List[int]:
    ans = []  
    starts = []
    ends = []
    for f in flowers:
        starts.append(f[0])
        ends.append(f[1] + 1)
    heapify(starts)
    heapify(ends)  
    cur = 0
    d = {_:people[_] for _ in range(len(people))}
    people = sorted(set(people))
    d2 = dict()
    for p in people:
        while starts and starts[0] <= p:
            heappop(starts)
            cur += 1
        while ends and ends[0] <= p:
            heappop(ends)
            cur -= 1
        d2[p] = cur
    for _ in d.values():
        ans.append(d2[_])
    return ans