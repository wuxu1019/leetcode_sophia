"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        head1, odd = head, head
        head2, even  = head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = head2
        return head1

    def oddEvenList2(self, head):
        dummy_odd = odd = ListNode(0)
        dummy_even = even = ListNode(0)

        while head:
            odd.next = head
            even.next = head.next
            odd = head
            even = head.next
            head = head.next.next if even else None

        odd.next = dummy_even.next
        return dummy_odd.next




if __name__ == '__main__':
    s = Solution()
    head = move = ListNode(0)
    for i in range(1, 8):
        move.next = ListNode(i)
        move = move.next
    rt = s.oddEvenList2(head.next)
    while rt:
        print rt.val
        rt = rt.next


