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

# https://leetcode.com/problems/word-search/description/
def exist(self, board: List[List[str]], word: str) -> bool:
    n = len(board) # row
    m = len(board[0]) # col
    def bt(i, j, word):
        if not word:
            return True
        if i < 0 or i == n or j < 0 or j == m:
            return False
        if word[0] != board[i][j]:
            return False
        board[i][j] = "*"
        for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if bt(i + row_offset, j + col_offset, word[1:]):
                return True
        board[i][j] = word[0]
        return False

    for i in range(n):
        for j in range(m):
            if bt(i, j, word):
                return True
    return False