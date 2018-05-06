'''
    From: LeetCode - 226. Invert Binary Tree
    Level: Easy
    Source: https://leetcode.com/problems/invert-binary-tree/description/
    Status: AC
	Solution: Using post-order traversal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        return root

# times o(n)
# space o(n)

'''
Most Optimal Answer: None

'''