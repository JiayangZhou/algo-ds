# https://leetcode.com/problems/integer-break
def integerBreak(self, n: int) -> int:
    memo = [-1] * (n + 1)
    memo[1] = 1
    def maxp(k):
        if memo[k] != -1 or k == 1:
            return memo[k]
        for i in range(1, k):
            memo[k] = max(maxp(i) * (k - i), memo[k], (k - i) * i)   
        return memo[k]         
    return maxp(n)