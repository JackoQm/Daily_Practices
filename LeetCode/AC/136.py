'''
    From: LeetCode - 136. Single Number
    Level: Easy
    Source: https://leetcode.com/problems/single-number/description/
    Status: AC
	Solution: Using Counter
'''

from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = Counter(nums)
        for k, v in res.items():
            if v == 1:
                return k

# times o(n)
# space o(n)

'''
Most Optimal Answer: Using exclusive or
class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            result ^= n
        return res

# times o(n)
# space o(1)
'''