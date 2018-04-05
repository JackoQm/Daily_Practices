'''
    From: LeetCode - 206. Reverse Linked List
    Level: Easy
    Question: Reverse a singly linked list.
	Status: AC
	Solution: Using Iterative
'''

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        newHead = ListNode(head.val)
        p = head.next
        while p is not None:
            tmp = p.next
            p.next = newHead
            newHead = p
            p = tmp
            
        return newHead

# times o(n)
# space o(1)

'''
Most Optimal Answer: No Better Solutions
'''