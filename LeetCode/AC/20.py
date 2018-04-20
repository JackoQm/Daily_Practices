'''
    From: LeetCode - 20. Valid Parentheses
    Level: Easy
    Source: https://leetcode.com/problems/valid-parentheses/description/
    Status: AC
	Solution: Using Stack
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isEq(l,r):
            if (l == '(' and r == ')') or (l == '[' and r == ']') or (l == '{' and r == '}'):
                return True
            return False
        pre = ['(','[','{']
        stack = []
        for c in s:
            # print(stack)
            if len(stack) == 0 or c in pre:
                stack.append(c)
            elif not isEq(stack[-1], c):
                return False
            else:
                stack.pop()
        return stack == []

# times o(n)
# space o(n)

'''
Most Optimal Answer: Better Logic
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

# times o(n)
# space o(n)
'''