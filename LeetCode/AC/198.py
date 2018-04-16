'''
    From: LeetCode - 198. House Robber
    Level: Easy
    Source: https://leetcode.com/problems/house-robber/description/
    Status: AC
	Solution: Using Dynamic Planning
'''

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        d = [nums[i] for i in range(2)]
        d.append(d[0]+nums[2])
        for i in range(3, len(nums)):
            j = i-2
            n = nums[i] + (d[j] if d[j] > d[j-1] else d[j-1])
            d.append(n)
        last = len(nums)-1
        return d[last] if d[last] > d[last-1] else d[last-1]

# times o(n)
# space o(n)

'''
Most Optimal Answer: 
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, e = 0, 0     # i = include current horse, e = exclude current horse
        for m in nums:
            tmp = i     # Use to store previous include situation in order to calculate 'e'
            i = m + e
            e = max(e, tmp)
        return max(i,e)

# times o(n)
# space o(1)
'''