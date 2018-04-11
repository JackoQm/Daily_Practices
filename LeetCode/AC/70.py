'''
    From: LeetCode - 70. Climbing Stairs
    Level: Easy
    Source: https://leetcode.com/problems/climbing-stairs/description/
    Status: AC
	Solution: Using recursion with memorization
'''

class Solution:
    m = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is 0 or n is 1:
            return 1
        if n in self.m:
            return self.m[n]
        self.m[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.m[n]

# times o(n)
# space o(n)

'''
Most Optimal Answer:
public class Solution {
    public int climbStairs(int n) {
        double sqrt5=Math.sqrt(5);
        double fibn=Math.pow((1+sqrt5)/2,n+1)-Math.pow((1-sqrt5)/2,n+1);
        return (int)(fibn/sqrt5);
    }
}

# times o(logn)
# space o(1)
'''