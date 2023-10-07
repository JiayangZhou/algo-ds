# https://leetcode.com/problems/integer-break
def integerBreak(self, n: int) -> int:
    dp = [1] * (n + 1)
    # 2 3 4 5 6 
    # 1 2 4 6 9
    for i in range(3, n + 1):
        for j in range(1, i):
            dp[i] = max((i - j) * j, dp[i], j * dp[i - j])
    return dp[n]

