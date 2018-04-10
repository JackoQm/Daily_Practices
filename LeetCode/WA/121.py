'''
    From: LeetCode - 121. Best Time to Buy and Sell Stock
    Level: Easy
    Question: Say you have an array for which the ith element is the price of a given stock on day i.
              If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
	Status: Time Limit Exceeded
	Solution: Using Brute Force
'''

# 这是正确的答案
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) is 0:
            return 0
        minNum = prices[0]
        profit = 0
        for price in prices:
            if price < minNum:
                minNum = price
            elif (price - minNum) > profit:
                profit = (price - minNum)
        return profit

# times o(n)
# space o(1)

'''
Most Optimal Answer: Above

'''