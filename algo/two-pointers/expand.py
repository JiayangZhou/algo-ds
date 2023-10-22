from typing import List
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/
def maximumScore(nums: List[int], k: int) -> int:
    left = k
    right = k
    n = len(nums)
    ans = minimum = nums[k]
    while left > 0 or right < n - 1:
        # this will miss one corner case when left is 0 and right is n - 1 
        # ans = max(ans, (right - left + 1) * minimum)
        if left > 0 and right < n - 1:
            if nums[left - 1] >= nums[right + 1]:
                left -= 1
            else:
                right += 1
        elif left > 0:
            left -= 1
        else:
            right += 1 
        minimum = min(minimum, min(nums[left], nums[right]))
        ans = max(ans, (right - left + 1) * minimum)
    return ans