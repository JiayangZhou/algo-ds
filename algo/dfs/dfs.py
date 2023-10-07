from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# inorder traversal, left subtree, root, right subtree
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traversal(node):
            if not node:
                return
            if node.left:
                traversal(node.left)
            res.append(node.val)
            if node.right:
                traversal(node.right)
        traversal(root)
        return res

# https://leetcode.com/problems/binary-tree-preorder-traversal/
# preorder traversal, root, left subtree, right subtree
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    def traversal(node):
        if not node:
            return
        res.append(node.val)
        if node.left:
            traversal(node.left)
        if node.right:
            traversal(node.right)
    traversal(root)
    return res

# https://leetcode.com/problems/binary-tree-preorder-traversal/
# postorder traversal, root, left subtree, right subtree
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    def traversal(node):
        if not node:
            return
        if node.left:
            traversal(node.left)
        if node.right:
            traversal(node.right)
        res.append(node.val)
    traversal(root)
    return res

# https://leetcode.com/problems/binary-tree-level-order-traversal
# level order traversal
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    d = {_:[] for _ in range(2001)}
    def traversal(node, level):
        if not node:
            return
        d[level].append(node.val)
        if node.left:
            traversal(node.left, level + 1)
        if node.right:
            traversal(node.right, level + 1)
    traversal(root, 0)
    res = []
    for v in d.values():
        if not v:
            break
        res.append(v)
    return res