import sys
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
def largestValues(root: Optional[TreeNode]) -> List[int]:
    queue = [root]
    ans = []
    if not root:
        return ans
    while queue:
        maxOfRow = -sys.maxsize
        for i in range(len(queue)):
            cur = queue.pop(0)
            maxOfRow = max(maxOfRow, cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        ans.append(maxOfRow)
    return ans

    # d = OrderedDict()
    # def dfs(node, level):
    #     if not node:
    #         return 
    #     if level not in d:
    #         d[level] = node.val
    #     else:
    #         d[level] = max(d[level], node.val)
    #     dfs(node.left, level + 1)
    #     dfs(node.right, level + 1)
    # dfs(root, 0)
    # ans = [_[1] for _ in d.items()]
    # return ans