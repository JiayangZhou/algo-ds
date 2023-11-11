# https://leetcode.com/problems/time-based-key-value-store
# binary search can be performed differently, depending on
# how you round mid, either ceil, towards right, or floor, towards left
class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
    def get_bs_ceil(self, key: str, timestamp: int) -> str:
        record = self.store[key]
        left = 0
        right = len(record) - 1
        while left < right:
            import math
            mid = math.ceil((left + right) / 2)
            if timestamp < record[mid][0]:
                right = mid - 1
            else:
                left = mid
        if not record or timestamp < record[0][0]:
            return ""
        return record[left][1]
        
    def get_bs_floor(self, key: str, timestamp: int) -> str:
        record = self.store[key]
        left = 0
        right = len(record) - 1
        while left < right:
            mid = (left + right) >> 1
            if timestamp > record[mid][0]:
                left = mid + 1
            else:
                right = mid
        if not record or timestamp < record[0][0]:
            return ""
        if timestamp < record[left][0]:
            return record[left - 1][1]
        return record[left][1]
