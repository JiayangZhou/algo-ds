from typing import List
# https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
# https://leetcode.com/problems/length-of-the-longest-valid-substring
# Trie implementation
def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
    t = Trie()
    for _ in forbidden:
        t.insert(_)
    ans = 0
    start = 0 
    for i in range(len(word)):
        for j in range(max(start, i - 9), i + 1):
            if t.search(word[j:i + 1]):
                start = j + 1
        ans = max(ans, i + 1 - start)
    return ans

# another solution
class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False
class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.head
        for c in word:
            if not c in temp.child:
                temp.child[c] = TrieNode()
            temp = temp.child[c]
        temp.isEnd = True
        
        
    def search(self, word: str) -> bool:
        temp = self.head
        for c in word:
            if not c in temp.child:
                return False
            temp = temp.child[c]
        return temp.isEnd

    def startsWith(self, prefix: str) -> bool:
        temp = self.head
        for c in prefix:
            if not c in temp.child:
                return False
            temp = temp.child[c]
        return True
