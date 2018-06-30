"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these two functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.MOD = 1000
        self.data = [None] * self.MOD

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if not self.contains(key):
            pos = key % self.MOD
            if not self.data[pos]:
                self.data[pos] = ListNode(key)
                return
            p = self.data[pos]
            while p.next:
                p = p.next
            p.next = ListNode(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        pos = key % self.MOD
        if self.contains(key):
            dummy = ListNode(0)
            dummy.next = self.data[pos]
            p = dummy
            while p.next.val != key:
                p = p.next
            p.next = p.next.next
            self.data[pos] = dummy.next
            return

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        pos = key % self.MOD
        if not self.data[pos]:
            return False
        p = self.data[pos]
        while p:
            if p.val == key:
                return True
            p = p.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)