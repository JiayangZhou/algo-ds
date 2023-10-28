from typing import List
from heapq import heappop, heappush
# https://leetcode.com/problems/count-the-number-of-k-big-indices/
# unlike min heap, we utilize max heap here
def kBigIndices(nums: List[int], k: int) -> int:
    n = len(nums)
    memo = [0] * n
    heap = []
    for i in range(n):
        cur = nums[i]
        if len(heap) == k and -heap[0] < cur:
            memo[i] = 1
        heappush(heap, -cur)
        if len(heap) > k:
            heappop(heap)
    heap = []
    ans = 0
    for i in range(n - 1, -1, -1):
        cur = nums[i]
        if len(heap) == k and -heap[0] < cur and memo[i]:
            ans += 1
        heappush(heap, -cur)
        if len(heap) > k:
            heappop(heap)
    return ans