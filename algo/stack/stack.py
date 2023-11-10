# https://leetcode.com/problems/valid-parentheses/
def isValid(self, s: str) -> bool:
    d = {'(':')', '{':'}','[':']'}
    stack = []
    for _ in s:
        if _ in d:  
            stack.append(_)
        else:
            if not stack:
                return False
            last = stack.pop()
            if last not in d:
                return False
            if d[last] != _:
                return False
    return len(stack) == 0

# https://leetcode.com/problems/daily-temperatures/
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # monotonic stack
    # time complexity -> O(2 * n)
    # stack only pop every element once
    # space complexity -> worst case -> O(n)
    stack = []
    ans = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            popped = stack.pop()
            ans[popped] = i - popped
        stack.append(i)
    return ans


    # O(n * 70)
    n = len(t)
    ans = [0] * n
    record = defaultdict(lambda: 10 ** 5 + 7)
    for i in range(n - 1, -1, -1):
        record[t[i]] = i
        low = 10 ** 5 + 7
        for j in range(t[i] + 1, 101):
            low = min(low, record[j])
        
        if low != 10 ** 5 + 7:
            ans[i] = low - i
    return ans