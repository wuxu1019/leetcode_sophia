import unittest

#Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = self.getString(l1)
        s2 = self.getString(l2)
        carry, head = 0, None
        i, j = 0, 0
        while s1 or s2 or carry:
            a, b = 0, 0
            if s1:
                a = s1.pop()
            if s2:
                b = s2.pop()
            val = carry + a + b
            carry = 1 if val / 10 else 0
            temp = head
            head = ListNode(val % 10)
            head.next = temp
        return head

    def getString(self, head):
        rt = []
        while head:
            rt.append(head.val)
            head = head.next
        return rt


class TestAddTwoNumbers(unittest.TestCase):
    def builduplistfromlist(self, l):
        head = ListNode(0)
        dummy = head
        while l:
            head.next = ListNode(l.pop())
            head = head.next
        return dummy.next

    def samelist(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1, l2 = l1.next, l2.next
        if l1 or l2:
            return False
        else:
            return True

    def printlist(self, l):
        list = []
        while l:
            list.append(l.val)
            l = l.next
        print list

    def setUp(self):
        self.s = Solution()
        pass

    def tearDown(self):
        pass

    def testCase1(self):
        l1 = self.builduplistfromlist([3, 4, 2, 7])
        l2 = self.builduplistfromlist([4, 6, 5])
        l3 = self.s.addTwoNumbers(l1, l2)
        self.printlist(l1)
        self.printlist(l2)
        self.printlist(l3)
        result = self.samelist(l3, self.builduplistfromlist([7, 0, 8, 7]))
        self.assertTrue(result)

    def testCase2(self):
        l1 = self.builduplistfromlist([3, 4, 2, 7])
        l2 = self.builduplistfromlist([4, 6, 5 ,8])
        l3 = self.s.addTwoNumbers(l1, l2)
        self.printlist(l3)
        result = self.samelist(l3, self.builduplistfromlist([7, 0, 8, 5, 1]))
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

