"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.


"""

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.xor = 0

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        newnode = ListNode(element)
        newaddr = dereference_pointer(newnode)

        if not self.head and not self.tail:
            self.head, self.tail = newnode, newnode
            return
        self.tail.xor ^= newaddr
        self.tail = newnode
        return

    def get(self, index):
        pre, cur = 0, self.head
        start = 0
        while start < index and cur != self.tail:
            pre, cur = dereference_pointer(cur), get_pointer(pre ^ cur.xor)
            start += 1
        if start == index:
            return cur.val
        else:
            return None

if __name__ == '__main__':
    l = LinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    rt1 = l.get(0)
    rt2 = l.get(1)
    rt3 = l.get(2)
    rt4 = l.get(3)
    print rt1, rt2, rt3, rt4

