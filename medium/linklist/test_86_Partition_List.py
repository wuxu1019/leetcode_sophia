"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition_one_dummy(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.val < x:
            p = p.next
        if not p.next:
            return dummy.next
        q = p.next
        m = q.next
        while m:
            if m.val >= x:
                m = m.next
                q = q.next
            else:
                q.next = m.next
                temp = p.next
                p.next = m
                m.next = temp
                p = m
                m = q.next
        return dummy.next

    def partition_two_dummy(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1 = p1 = ListNode(0)
        dummy2 = p2 = ListNode(0)

        while head:
            if head.val >= x:
                p2.next = head
                p2 = p2.next
            else:
                p1.next = head
                p1 = p1.next
            head = head.next

        p2.next = None
        p1.next = dummy2.next
        return dummy1.next