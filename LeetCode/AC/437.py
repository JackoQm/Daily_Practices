'''
    From: LeetCode - 437. Path Sum III
    Level: Easy
    Source: https://leetcode.com/problems/path-sum-iii/description/
    Status: AC
	Solution: Using BFS
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def findPath(root, add, sum):
            if not root:
                return 0
            add += root.val
            
            return findPath(root.left, add, sum) + findPath(root.right, add, sum) + (1 if add == sum else 0)
        
        if not root:
            return 0
        queue = deque([root])
        result = 0
        while len(queue) != 0:
            node = queue.popleft()
            result += findPath(node, 0, sum)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result 

# times o(n^2)
# space o(n)

'''
Most Optimal Answer: Two sum method
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def helper(self, root, target, so_far, cache):
            if root:
                so_far += root.val
                complement = so_far - target
                self.result += cache.get(complement, 0)
                cache[so_far] = 1
                self.helper(root.left, target, so_far, cache)
                self.helper(root.right, target, so_far, cache)
                cache[so_far] -= 1
            return
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result

# times o(n)
# space o(n)
'''