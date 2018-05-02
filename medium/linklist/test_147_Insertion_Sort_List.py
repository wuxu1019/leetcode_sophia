# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList_n2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        complete = ListNode(-float('INF'))
        complete.next = None

        while head:
            head, target = head.next, head
            target.next = None
            complete = self.insertOneNode(complete, target)
        return complete.next

    def insertOneNode(self, h, node):
        head = h
        while head.next and node.val > head.next.val:
            head = head.next
        node.next, head.next = head.next, node
        return h

    def insertionSortList_nlogn(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        record = []
        while head:
            head, target = head.next, head
            target.next = None
            self.insertOneNode2(record, target)
        for i in range(len(record) - 1):
            record[i].next = record[i + 1]
        return record[0]

    def insertOneNode2(self, l, target):
        if not l:
            l.append(target)
            return
        lo, hi = 0, len(l) - 1
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            if l[mid].val > target.val:
                hi = mid - 1
            else:
                lo = mid + 1
        l.insert(lo, target)

    def insertionSortList_n2_better(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        while cur and cur.next:
            p = dummy
            cur_next = cur.next
            val = cur.next.val
            if val >= cur.val:
                cur = cur.next
                continue
            while p.next.val < val:
                p = p.next
            temp = p.next
            cur.next = cur_next.next
            p.next = cur_next
            cur_next.next = temp

        return dummy.next