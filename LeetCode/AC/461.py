'''
    From: LeetCode - 461. Hamming Distance
    Level: Easy
    Source: https://leetcode.com/problems/hamming-distance/description/
    Status: AC
	Solution: Using exclusive or
'''

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        num = x ^ y
        count = 0
        while num != 0:
            if num % 2 == 1:
                count += 1
            num //= 2
        return count

# times o(n)
# space o(1)

'''
Most Optimal Answer:
class Solution:
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')

# times o(n)
# space o(1)
'''