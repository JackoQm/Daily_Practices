'''
    From: LeetCode - 104. Maximum Depth of Binary Tree
    Level: Easy
    Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
    Status: AC
	Solution: Using Recrusive
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findDepth(root, depth):
            if not root:
                return depth
            return max(findDepth(root.left, depth+1), findDepth(root.right, depth+1))
        return findDepth(root, 0)

# times o(nlogn)
# space o(m)

'''
Most Optimal Answer: Using exclusive or
class Solution:
    def maxDepth(self, root):
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

'''