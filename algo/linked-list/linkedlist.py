from tkinter.tix import ListNoteBook
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
class Solution:
    def pairSum(self, head: Optional[ListNoteBook]) -> int:
        dq = []
        maxs = 0
        while head:
            dq.append(head.val)
            head = head.next
        while(dq):
            maxs = max(maxs, dq.pop() + dq.pop(0))
        return maxs
    
# https://leetcode.com/problems/merge-two-sorted-lists/description/
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    head = dummy
    while list1 and list2:
        if list1.val < list2.val:
            head.next = ListNode(list1.val)
            head = head.next
            list1 = list1.next
        else:
            head.next = ListNode(list2.val)
            head = head.next
            list2 = list2.next
    if list1:
        head.next = list1
    elif list2:
        head.next = list2
    return dummy.next