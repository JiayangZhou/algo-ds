from typing import List
import sys
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days
def shipWithinDays(weights: list[int], days: int) -> int:
    # low = max(weights)
    # high = sum(weights)
    low = 1
    high = sys.maxsize - 100000
    def check(ship):
        s = ship
        d = 1
        for w in weights:
            if w <= s:
                s -= w
            else:
                d += 1
                s = ship - w
                if d > days or s < 0:
                    return False
        return d <= days
    while low < high:
        mid = (low + high) >> 1
        if not check(mid):
            low = mid + 1
        else:
            high = mid
    return high

# shipWithinDays([1,2,3,1,1], 4) # 3
# shipWithinDays([3,2,2,4,1,4], 3) # 6

# https://leetcode.com/problems/random-pick-with-weight/
class Solution:
    def __init__(self, w: List[int]):
        self.arr = []
        self.cur = 0
        for _ in w:
            self.cur += _
            self.arr.append(self.cur)
        
    def pickIndex(self) -> int:
        import random
        r = random.randint(1, self.cur)
        left = 0
        right = len(self.arr) - 1
        while left < right:
            mid = (left + right) >> 1
            if self.arr[mid] < r:
                left = mid + 1
            else:
                right = mid
        return left
# obj = Solution([3,14,1,7])
# param_1 = obj.pickIndex()
# print(param_1)