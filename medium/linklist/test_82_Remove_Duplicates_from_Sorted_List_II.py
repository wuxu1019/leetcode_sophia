"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(float('INF'))
        p, i, j = dummy, head, head.next
        while j:
            if i.val != j.val:
                if j == i.next:
                    p.next = i
                    p = p.next
                    i = i.next
                    p.next = None
                else:
                    i = j
            j = j.next
        if not i.next:
            p.next = i
        return dummy.next
