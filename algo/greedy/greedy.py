from typing import List
# https://leetcode.com/problems/valid-palindrome-ii/
# two pointers
def validPalindrome(self, s: str) -> bool:
    p1 = 0
    n = len(s)
    p2 = n - 1
    while p1 < p2:
        if s[p1] != s[p2]:
            s1 = s[:p1] + s[p1 + 1:]
            s2 = s[:p2] + s[p2 + 1:]
            return s1 == s1[::-1] or s2 == s2[::-1]
        p1 += 1
        p2 -= 1
    return True

# https://leetcode.com/problems/lemonade-change
def lemonadeChange(bills: list[int]) -> bool:
    hand = {5:0, 10:0}
    for b in bills:
        if b == 5:
            hand[5] += 1
        elif b == 10:
            if not hand[5]:
                return False
            else:
                hand[5] -= 1
                hand[10] += 1
        else:
            if hand[10] and hand[5]:
                hand[5] -= 1
                hand[10] -= 1
            elif hand[5] >= 3:
                hand[5] -= 3
            else:
                return False
    return True
# lemonadeChange(bills=[5,5,10,10,20])

# https://leetcode.com/problems/mice-and-cheese/
from heapq import heapify, heappush, heappop
def miceAndCheese(reward1: List[int], reward2: List[int], k: int) -> int:
    n = len(reward1)
    diff = []
    for i in range(n):
        diff.append((reward1[i] - reward2[i], i))
    heapify(diff)
    res = 0
    while n - k > 0:
        cur = heappop(diff)
        res += reward2[cur[1]]
        k += 1
    while diff:
        cur = heappop(diff)
        res += reward1[cur[1]]
    return res