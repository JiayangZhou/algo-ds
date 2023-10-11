from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# https://leetcode.com/problems/maximum-binary-tree/
def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    def build(arr):
        arrmax = max(arr)
        index = arr.index(arrmax)
        node = TreeNode(arrmax)
        if arr[:index]:
            node.left = build(arr[:index])
        if arr[index + 1:]:
            node.right = build(arr[index + 1:])  
        return node
    return build(nums)