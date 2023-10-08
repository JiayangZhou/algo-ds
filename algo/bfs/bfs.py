from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# https://leetcode.com/problems/path-sum-ii/
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    res = []
    if not root:
        return res
    queue = [(root, [], 0)]
    while queue:
        n = len(queue)
        for i in range(n):
            cur = queue.pop(0)
            if cur[0].left:
                queue.append((cur[0].left, cur[1] + [cur[0].val], cur[2] + cur[0].val))
            if cur[0].right:
                queue.append((cur[0].right, cur[1] + [cur[0].val], cur[2] + cur[0].val))
            if not cur[0].left and not cur[0].right:
                if cur[0].val + cur[2] == targetSum:
                    res.append(cur[1] + [cur[0].val])
    return res


