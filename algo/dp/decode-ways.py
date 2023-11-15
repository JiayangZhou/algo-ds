# https://leetcode.com/problems/decode-ways/
def numDecodings(self, s: str) -> int:
    # top down + memorization
    # time complexity O(n)
    # space complexity O(n)
    n = len(s)
    record = set([str(_) for _ in range(1, 27)])
    memo = [-1] * (n + 1)
    def dp(index):
        if index == n:
            return 1
        if s[index] not in record:
            return 0
        if index < n - 1 and s[index: index + 2] in record:
            if memo[index + 1] != -1:
                a = memo[index + 1]
            else:
                a = dp(index + 1)
                memo[index + 1] = a

            if memo[index + 2] != -1:
                b = memo[index + 2]
            else:
                b = dp(index + 2)
                memo[index + 2] = b
            return a + b
        else:
            if memo[index + 1] != -1:
                a = memo[index + 1]
            else:
                a = dp(index + 1)
                memo[index + 1] = a
            return a
    return dp(0)

    # bottom up
    # time complexity O(n)
    # space complexity O(n)
    n = len(s)
    record = set([str(_) for _ in range(1, 27)])
    if s[0] not in record:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0
    if s[0:2] in record and s[1:2] in record:
        dp[1] = 2
    elif s[0:2] in record or s[1:2] in record:
        dp[1] = 1

    for i in range(2, n):
        if s[i] in record:
            dp[i] = dp[i - 1]
        if s[i - 1: i + 1] in record:
            dp[i] += dp[i - 2]
    return dp[n - 1]

    # top down
    # time complexity O(n)
    # space complexity O(n)
    n = len(s)
    record = set([str(_) for _ in range(1, 27)])
    @cache
    def dp(index):
        if index == n:
            return 1
        if s[index] not in record:
            return 0
        if index < n - 1 and s[index: index + 2] in record:
            return dp(index + 1) + dp(index + 2)
        else:
            return dp(index + 1)
    return dp(0)