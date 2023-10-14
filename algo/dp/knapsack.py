from typing import List, Optional
# https://leetcode.com/problems/painting-the-walls
def paintWalls(self, cost: List[int], time: List[int]) -> int:
    n = len(cost)
    import sys
    dp = [0] + [sys.maxsize] * n
    for c, t in zip(cost, time):
        for j in range(n, 0, -1):
            dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
    return dp[n]