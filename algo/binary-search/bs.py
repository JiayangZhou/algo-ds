# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days
import sys
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

