from typing import List
# https://leetcode.com/problems/length-of-the-longest-valid-substring/
def longestValidSubstring(word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        ans = 0
        start = 0 
        for i in range(len(word)):
            for j in range(max(start, i - 9), i + 1):
                if word[j:i + 1] in forbidden:
                    start = j + 1
            ans = max(ans, i + 1 - start)
        return ans