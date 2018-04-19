'''
    From: LeetCode - 141. Linked List Cycle
    Level: Easy
    Source: https://leetcode.com/problems/linked-list-cycle/description/
    Status: AC
	Solution: Using Hash Table
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        p = head.next
        m = {head}
        while p is not None:
            if p in m:
                return True
            m.add(p)
            p = p.next
        return False

# times o(n)
# space o(n)

'''
Most Optimal Answer: Two Pointers
def hasCycle(self, head):
    try:
        normalSpeed = head
        x2Speed = head.next
        while normalSpeed is not x2Speed:
            normalSpeed = normalSpeed.next
            x2Speed = x2Speed.next.next
            print('normal: {}, x2Speed: {}'.format(normalSpeed.val, x2Speed.val))
        return True
    except:
        return False

# times o(n)
# space o(1)
'''