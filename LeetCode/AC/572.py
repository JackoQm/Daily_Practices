'''
    From: LeetCode - 572. Subtree of Another Tree
    Level: Easy
    Source: https://leetcode.com/problems/subtree-of-another-tree/description/
    Status: AC
	Solution: Using Recursive Comparison
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def check(s, t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            return s.val == t.val and check(s.left, t.left) and check(s.right, t.right)
        
        if s is None or t is None:
            return False
        nodes = deque([s])
        while len(nodes) != 0:
            n = nodes.popleft()
            if n.val == t.val and check(n, t):
                return True
            if n.left is not None:
                nodes.append(n.left)
            if n.right is not None:
                nodes.append(n.right)
        return False

# times o(m * n)
# space o(n)

'''
Most Optimal Answer: Above
'''