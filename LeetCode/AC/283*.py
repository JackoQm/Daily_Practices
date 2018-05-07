'''
    From: LeetCode - 283. Move Zeroes
    Level: Easy
    Source: https://leetcode.com/problems/move-zeroes/description/
    Status: AC
	Solution: Using two pointer
'''

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        f, s = 0, 0
        length = len(nums)
        while s < length:
            if nums[s] != 0:
                if f != s:
                    nums[f] = nums[s]
                f += 1
            s += 1
        while f < length:
            nums[f] = 0
            f += 1

# times o(n)
# space o(1)

'''
Most Optimal Answer: 
class Solution:
    def moveZeroes(self, nums):
        last = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[last] = nums[last], nums[i]
                last += 1

# times o(n)
# space o(1)
'''