"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        kdata = [(l.val, i) for i, l in enumerate(lists) if l]
        rt = p = ListNode(0)
        heapq.heapify(kdata)
        while kdata:
            data, location = heapq.heappop(kdata)
            p.next = lists[location]
            p = p.next
            lists[location] = lists[location].next
            if lists[location]:
                heapq.heappush(kdata, (lists[location].val, location))
        return rt.next
