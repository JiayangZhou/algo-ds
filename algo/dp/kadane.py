# find the maximum subarray sum in an array of integers
def findMax(arr = [1, -2, 3, 4]):
    maxLocal = maxGlobal = 0
    for i in range(len(arr)):
        maxLocal += arr[i]
        maxGlobal = max(maxGlobal, maxLocal)
        if maxLocal < 0:
            maxLocal = 0
    return maxGlobal
print(findMax())

# https://leetcode.com/problems/substring-with-largest-variance/
def largestVariance(s: str) -> int:
    allElements = set()
    from collections import defaultdict
    d = defaultdict(lambda: 0)
    for _ in s:
        if _ not in allElements:
            allElements.add(_)
        d[_] += 1
    ans = 0
    allElements = list(allElements)
    for i in range(len(allElements)):
        major = allElements[i]
        for j in range(len(allElements)):
            if i == j:
                continue
            minor = allElements[j]
            remainMinor = d[minor]
            maxLocal = maxGlobal = 0
            seen = set()
            for _ in s:
                if _ == major:
                    maxLocal += 1
                    seen.add(_)
                elif _ == minor:
                    maxLocal -= 1
                    seen.add(_)
                    remainMinor -= 1
                else:
                    continue
                if maxLocal < 0 and remainMinor > 0:
                    maxLocal = 0
                    seen = set()
                if len(seen) == 2 and maxLocal > maxGlobal:
                    maxGlobal = maxLocal
            ans = max(ans, maxGlobal)

    return ans