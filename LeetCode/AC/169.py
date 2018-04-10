'''
    From: LeetCode - 169. Majority Element
    Level: Easy
    Question: Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
  		      You may assume that the array is non-empty and the majority element always exist in the array.
	Status: AC
	Solution: Using HashMap
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.hash = {}
        count = 0
        min_times = len(nums) // 2
        for num in nums:
            if num in self.hash:
                self.hash[num] += 1
            else:
                self.hash[num] = 1
        for num, times in self.hash.items():
            if times > min_times:
                return num

# times o(n)
# space o(n)

'''
Most Optimal Answer:

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            
        return candidate
'''
# times o(n)
# space o(1)