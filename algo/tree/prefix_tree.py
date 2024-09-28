from typing import List
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/?envType=daily-question&envId=2024-09-25

class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.children = [None] * 26
def sumPrefixScores(words: List[str]) -> List[int]:
    dummy = TreeNode()
    def traversal_build(node, s, index):
        if index == len(s):
            return
        if node.children[ord(s[index]) - ord('a')] is None:
            node.children[ord(s[index]) - ord('a')] = TreeNode(1)
        else:
            node.children[ord(s[index]) - ord('a')].val += 1
        traversal_build(node.children[ord(s[index]) - ord('a')], s, index + 1)
    for word in words:
        traversal_build(dummy, word, 0)
    def traversal_check(node, s, index):
        if index == len(s) - 1:
            return node.children[ord(s[index]) - ord('a')].val
        return traversal_check(node.children[ord(s[index]) - ord('a')], s, index + 1) + node.val
    arr = []
    for word in words:
        arr.append(traversal_check(dummy, word, 0))
    return arr
sumPrefixScores(words=["abc","ab","bc","b"])