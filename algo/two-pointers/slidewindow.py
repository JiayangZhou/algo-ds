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