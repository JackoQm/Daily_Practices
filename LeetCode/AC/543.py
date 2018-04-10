'''
    From: LeetCode - 543. Diameter of Binary Tree
    Level: Easy
    Question: Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
	Status: AC
	Solution: Using tree depth counting
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.countDepth(root.left)
        right = self.countDepth(root.right)
        longest = left + right
        if left > right:
            longest = max(longest, self.diameterOfBinaryTree(root.left))
        elif left < right:
            longest = max(longest, self.diameterOfBinaryTree(root.right))
        
        return longest
        
    def countDepth(self, root, depth=0):
        if not root:
            return depth
        depth += 1
        leftDepth = self.countDepth(root.left, depth)
        rightDepth = self.countDepth(root.right, depth)
        return max(leftDepth, rightDepth)

# times o(n)
# space o(n)

'''
Most Optimal Answer: No Better Solutions
'''