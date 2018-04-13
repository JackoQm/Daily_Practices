'''
    From: LeetCode - 101. Symmetric Tree
    Level: Easy
    Source: https://leetcode.com/problems/symmetric-tree/description/
    Status: Time Limited Exceeded
	Solution: Using Hierarchical traversal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = deque([root])
        depth = 1
        while len(q) != 0 and q.count(None) != len(q):
            child = []
            for i in range(depth):
                node = q.popleft()
                if node is None:
                    for _ in range(2):
                        q.append(None)
                        child.append(None)
                else :
                    if node.left is None:
                        child.append(None)
                    else:
                        child.append(node.left.val)
                    if node.right is None:
                        child.append(None)
                    else:
                        child.append(node.right.val)
                    q.append(node.left)
                    q.append(node.right)
            i = 0
            j = 2*depth - 1
            while i < j:
                if(child[i] != child[j]):
                    return False
                i += 1
                j -= 1
            depth *= 2
                
        return True

# times o(n)
# space o(n)

'''
Most Optimal Answer: Recursive
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(lnode, rnode):
            if not lnode and not rnode:
                return True
            if not lnode or not rnode:
                return False
            return (lnode.val == rnode.val) and check(lnode.right, rnode.left) and check (lnode.left, rnode.right)
        
        if not root:
            return True
        return check(root.left, root.right)

# times o(n)
# space o(n)
'''