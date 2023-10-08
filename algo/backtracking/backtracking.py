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
restoreIpAddresses("25525511135")



