from typing import List, Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous
def minOperations(nums: List[int]) -> int:
        n = len(nums)
        diff = n - 1
        a = sorted(list(set(nums)))
        maxsubarr = 1
        slow = 0
        fast = len(a) - 1
        fast = 0
        while slow < len(a) or fast < len(a):
            while fast < len(a) and a[fast] - a[slow] <= diff:
                fast += 1
            maxsubarr = max(maxsubarr, fast - slow)
            slow += 1
        return n - maxsubarr
    
# https://leetcode.com/problems/linked-list-cycle
def hasCycle(head: Optional[ListNode]) -> bool:
    p1 = head
    p2 = head
    while p2 and p2.next != None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False