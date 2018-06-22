"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight_twopoint1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        lth = 0
        while head:
            lth += 1
            head = head.next
        k = k % lth
        if not k:
            return dummy.next
        a, b = dummy, dummy
        while k:
            b = b.next
            k -= 1
        while b.next:
            a, b = a.next, b.next
        dummy.next, b.next = a.next, dummy.next
        a.next = None
        return dummy.next

    def rotateRight_twopoint2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or not k:
            return head
        lth = 1
        p = head
        while p.next:
            p = p.next
            lth += 1
        k = k % lth
        if not k:
            return head

        fast, slow = head, head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast, slow = fast.next, slow.next
        temp = slow.next
        slow.next = None
        fast.next = head
        head = temp
        return head

    def rotateRight_connect_tail_to_head(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k or not head.next:
            return head
        lth = 1
        tail = head
        while tail.next:
            lth += 1
            tail = tail.next
        tail.next = head
        k = k % lth
        for _ in range(lth - k):
            tail = tail.next

        head = tail.next
        tail.next = None
        return head



