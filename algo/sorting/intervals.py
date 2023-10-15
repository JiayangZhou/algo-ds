from typing import List
# https://leetcode.com/problems/merge-intervals
def merge(self, a: List[List[int]]) -> List[List[int]]:
    ans = []
    n = len(a)
    a = sorted(a, key=lambda x: (x[0], x[1]))
    l = a[0][0]
    r = a[0][1]
    for i in range(1, n):
        cur = a[i]
        if r < cur[0]:
            ans.append([l, r])
            l = cur[0]
            r = cur[1]
        else:
            r = max(cur[1], r)
    ans.append([l, r])
    return ans

# https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms-ii
from heapq import heapify, heappop, heappush
def meetingRoom(a):
    s = []
    e = []
    for _ in a:
        s.append(_[0])
        e.append(_[1])
    heapify(s)
    heapify(e)
    rooms = 0
    free = 0
    while s and e:
        if s[0] < e[0]:
            heappop(s)
            if free > 0:
                free -= 1
            else:
                rooms += 1
        else:
            heappop(e)
            free += 1
    return rooms
    
meetingRoom([[0, 30],[5, 10],[15, 20]])