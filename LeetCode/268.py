'''
    From: LeetCode - 268. Missing Number
    Level: Easy
    Question: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
	Status: AC
	Solution: Using HashMap
'''

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0] * (len(nums) + 1)
        for n in nums:
            res[n] = 1
        return res.index(0)

# times o(n)
# space o(n)

'''
Most Optimal Answer: 

1、Gauss' Formula：
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# times o(n)
# space o(1)

2、Bit Manipulation
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

# times o(n)
# space o(1) 
'''