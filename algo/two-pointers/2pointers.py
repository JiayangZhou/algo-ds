from typing import List, Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# https://leetcode.com/problems/container-with-most-water/
def maxArea(h: List[int]) -> int:
    res = 0
    n = len(h)
    left = 0
    right = n - 1
    while left < right:
        width = right - left
        height = min(h[left], h[right])
        res = max(res, height * width)
        if h[left] < h[right]:
            left += 1
        else:
            right -= 1
    return res

# https://leetcode.com/problems/3sum/
# 2sum can also use two pointers, just need to sort array first
def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    ans = []
    for i in range(n):
        t = -nums[i]
        l = i + 1
        r = n - 1
        while l < r:
            if nums[l] + nums[r] == t:
                _ = sorted([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                if _ not in ans:
                    ans.append(_)
            elif nums[l] + nums[r] > t:
                r -= 1
            else:
                l += 1
    return ans