# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
# dynamic-size slide window, bad performance on this one though
def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    d = {}
    n = len(s)
    diff = maxSize - minSize
    for i in range(n - minSize + 1):
        for j in range(i, i + diff + 1):
            if j + minSize > n:
                continue 
            cur = s[i:j + minSize]
            if len(set([*cur])) <= maxLetters:
                if cur not in d:
                    d[cur] = 1
                else:
                    d[cur] += 1
    if not d:
        return 0
    return sorted(d.items(), key=lambda x:x[1], reverse=True)[0][1]

# maxFreq("aababcaab", 2, 3, 4)
maxFreq("abcde", 2, 3, 3)

# improvement, maxSize does not need to be counted, 
# because number of minSize is always greater than the number of maxSize
def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    d = {}
    n = len(s)
    for i in range(n - minSize + 1):
        cur = s[i:i + minSize]
        if len(set([*cur])) <= maxLetters:
            if cur not in d:
                d[cur] = 1
            else:
                d[cur] += 1
    if not d:
        return 0
    return sorted(d.items(), key=lambda x:x[1], reverse=True)[0][1]

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# dynamic sliding window
def lengthOfLongestSubstring(self, s: str) -> int:
    set1 = set()
    last = 0
    ans = 0
    for i in range(len(s)):
        cur = s[i]
        if cur not in set1:
            set1.add(cur)
        else:
            for j in range(last, i):
                if s[j] == cur:
                    last = j + 1
                    break
                else:
                    set1.discard(s[j])
        ans = max(ans, i - last + 1)
    return ans

# https://leetcode.com/problems/constrained-subsequence-sum
def constrainedSubsetSum(nums, k):
    n = len(nums)
    deque = []
    for i in range(n):
        while(deque and deque[0] < i - k):
            deque.pop(0)
        if deque:
            nums[i] = nums[deque[0]] + nums[i]

        while(deque and nums[deque[-1]] < nums[i]): 
            deque.pop()

        if nums[i] > 0: 
            deque.append(i)
    return max(nums)
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = nums[0]
    memo = [dp[0]]
    ans = dp[0]
    for i in range(1, n):
        dp[i] = nums[i] + max(max(memo), 0)
        if len(memo) == k:
            memo.pop(0)
            memo.append(dp[i])
        else:
            memo.append(dp[i])
        ans = max(ans, dp[i])
    return ans
# constrainedSubsetSum([10,2,-3,-8,5,20], 3)