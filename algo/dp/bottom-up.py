# https://leetcode.com/problems/integer-break
def integerBreak(self, n: int) -> int:
    dp = [1] * (n + 1)
    # 2 3 4 5 6 
    # 1 2 4 6 9
    for i in range(3, n + 1):
        for j in range(1, i):
            dp[i] = max((i - j) * j, dp[i], j * dp[i - j])
    return dp[n]

# https://leetcode.com/problems/maximize-the-profit-as-the-salesman/
def maximizeTheProfit(n: int, offers: List[List[int]]) -> int:
    dp = [0] * n
    p = [[] for _ in range(n)]
    for _ in offers:
        s,e,g = _[0], _[1], _[2]
        p[e].append([s, g])
    for i in range(n):
        for _ in p[i]:
            s = _[0]
            g = _[1]
            dp[i] = max(dp[i], dp[s - 1] + g)
        dp[i] = dp[i - 1] if dp[i] < dp[i - 1] else dp[i]
    return dp[n - 1]

