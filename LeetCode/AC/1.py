'''
    From: LeetCode - 1. Two Sum
    Level: Easy
    Source: https://leetcode.com/problems/two-sum/description/
    Status: AC
	Solution: Using Hash Table
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            cha = target - nums[i]
            if cha in dic and dic[cha] != i:
                return [i, dic[cha]]

# times o(n)
# space o(n)

'''
Most Optimal Answer: Above

'''