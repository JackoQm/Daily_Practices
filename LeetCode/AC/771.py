'''
    From: LeetCode - 771. Jewels and Stones
    Level: Easy
    Source: https://leetcode.com/problems/jewels-and-stones/description/
    Status: AC
	Solution: Using Counter
'''

from collections import Counter
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dic = Counter(S)
        count = 0
        for ch in J:
            count += dic[ch]
        return count

# times o(n)
# space o(m)

'''
Most Optimal Answer:
class Solution(object):
    def numJewelsInStones(self, J, S):
    return sum(map(J.count, S))

# times o(n)
# space o(n)
'''