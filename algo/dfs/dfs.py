from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# inorder traversal, left subtree, root, right subtree
class Solution:
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
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
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
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
def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
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
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
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

# https://leetcode.com/problems/subsets-ii/
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    def dfs(index, subset):
        _ = sorted(subset.copy())
        if _ not in res:
            res.append(_)
        for i in range(index, n):
            dfs(i + 1, subset + [nums[i]])
    dfs(0, [])
    return sorted(res)
# subsetsWithDup([1,2,2])

# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii
# subsequence problem
# not so optimized, TLE ERROR
def getWordsInLongestSubsequence(n: int, words: List[str], groups: List[int]) -> List[str]:
    ans = []
    d = {words[i]: i for i in range(n)}
    def check(s1, s2):
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
            if diff > 1:
                return False
        return True
    def dfs(index, sub):
        nonlocal ans
        if len(sub) > len(ans):
            ans = sub.copy()
        if index >= n:
            return
        for i in range(index + 1, n):
            if groups[d[words[index]]] != groups[i] and len(words[i]) == len(words[index]) and check(words[i], words[index]):
                dfs(i, sub + [words[i]])
    for i in range(n):
        dfs(i, [words[i]])

    return ans
getWordsInLongestSubsequence(4, ["a","b","c","d"], [1,2,3,4])
# getWordsInLongestSubsequence(6, ["cba","cc","cd","ccc","aba","ac"], [3,6,2,4,2,6])