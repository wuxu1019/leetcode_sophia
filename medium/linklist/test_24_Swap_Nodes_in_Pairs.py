"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = head
        pre = dummy
        while p and p.next:
            temp = p.next
            p.next, temp.next = temp.next, p
            pre.next = temp
            pre = p
            p = p.next
        return dummy.next

    def swapPairs_recuisive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp