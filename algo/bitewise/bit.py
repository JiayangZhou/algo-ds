from typing import List

# https://leetcode.com/contest/biweekly-contest-141/problems/construct-the-minimum-bitwise-array-ii/

def minBitwiseArray(nums: List[int]) -> List[int]:
    res = []
    for num in nums:
        if num == 2:
            res.append(-1)
            continue
        bit_string = bin(num)[2:]
        last_one_index = -1
        for i in range(len(bit_string) - 1, -1 ,-1):
            if bit_string[i] == "1":
                last_one_index = i
                continue
            else:
                if i == len(bit_string) - 1:
                    break
                last_one_index = i + 1
                break
        new_bit_string = bit_string[:last_one_index] + '0' + bit_string[last_one_index + 1:]
        temp = int(new_bit_string, 2)
        if temp == 0:
            res.append(-1)
        else:
            res.append(temp)

    return res
minBitwiseArray(nums=[2,3,5,7])