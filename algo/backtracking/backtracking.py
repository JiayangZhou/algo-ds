from typing import List, Optional
# https://leetcode.com/problems/restore-ip-addresses/
def restoreIpAddresses(s: str) -> List[str]:
        set1 = {str(_) for _ in range(256)}
        n = len(s)
        res = []
        def bt(index, l):
            if index >= n or len(l) > 4:
                if len(l) == 4:
                    res.append(".".join(l))
                return
            last = l.pop()
            if last + s[index] in set1:
                bt(index + 1, l + [last + s[index]])
            bt(index + 1, l + [last] + [s[index]])
        bt(1, [s[0]])
        return res
# restoreIpAddresses("25525511135")

# https://leetcode.com/problems/word-break-ii/
def wordBreak(s: str, wd: List[str]) -> List[str]:
    res = []
    n = len(s)
    def bt(index, arr):
        if index >= n:
            if arr[-1] in wd:
                res.append(" ".join(arr))
            return
        last = arr.pop()
        if last in wd:
            bt(index + 1, arr + [last] + [s[index]])
        bt(index + 1, arr + [last + s[index]])

    bt(1, [s[0]])
    return list(set(res))
wordBreak(s="pineapplepenapple", wd=["apple","pen","applepen","pine","pineapple"])

