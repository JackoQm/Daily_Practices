'''
    From: LeetCode - 21. Merge Two Sorted Lists
    Level: Easy
    Source: https://leetcode.com/problems/merge-two-sorted-lists/description/
    Status: AC
	Solution: Using built-in list methods
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newL = None
        if not l1:
            return l2
        elif not l2:
            return l1
        
        def toList(result, l):
            while l:
                result.append(l.val)
                l = l.next
        
        def toListNode(l):
            result = ListNode(l[0])
            p = result
            for i in range(1,len(l)):
                n = ListNode(l[i])
                p.next= n
                p = n
            return result
                
        result = []
        toList(result, l1)
        toList(result, l2)
    
        return toListNode(sorted(result))

# times o(n)
# space o(n)

'''
Most Optimal Answer:None
'''