from typing import List, Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# https://leetcode.com/problems/container-with-most-water/
def maxArea(h: List[int]) -> int:
    res = 0
    n = len(h)
    left = 0
    right = n - 1
    while left < right:
        width = right - left
        height = min(h[left], h[right])
        res = max(res, height * width)
        if h[left] < h[right]:
            left += 1
        else:
            right -= 1
    return res

# https://leetcode.com/problems/linked-list-cycle
def hasCycle(self, head: Optional[ListNode]) -> bool:
    p1 = head
    p2 = head
    while p2 and p2.next != None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False