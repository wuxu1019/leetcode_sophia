"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
Seen this question in a real interview before?

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pl, p = dummy, dummy.next

        i = 1
        while i < m:
            pl, p = pl.next, p.next
            i += 1
        leftmost = pl
        while i <= n:
            pr = p.next
            p.next = pl
            pl = p
            p = pr
            i += 1
        leftmost.next.next, leftmost.next = p, pl

        return dummy.next




