"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.


"""


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList_two_pass(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = {}
        m, n = head, head
        while m:
            dic[m] = RandomListNode(m.label)
            m = m.next

        while n:
            dic[n].next = dic.get(n.next, None)
            dic[n].random = dic.get(n.random, None)
            n = n.next
        return dic.get(head, None)

    def copyRandomList_on_dict(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        p = head
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            p.next = node
            p = p.next.next
            # p = node.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead