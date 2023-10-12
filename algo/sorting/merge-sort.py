class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# in-place merge sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) >> 1
 
        left = arr[:mid]
        right = arr[mid:]
    
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
arr = [3, 1, 5, 2, 6]
mergeSort(arr)
print(arr)

# https://leetcode.com/problems/sort-list/
# merge sort linked list
def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    # return the right
    def split(node):
        slow = node
        fast = node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(l, r):
        dummy = ListNode()
        cur = dummy
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        if l:
            cur.next =l
        elif r:
            cur.next = r
        return dummy.next
    left = head
    right = split(head)
    temp = right.next
    right.next = None
    right = temp
    left = self.sortList(left)
    right = self.sortList(right)
    return merge(left, right)