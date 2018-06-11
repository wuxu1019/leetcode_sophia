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
        self.head = ListNode(0)

    def add(self, element):
        pre, point = dereference_pointer(self.head), self.head.xor
        while point.xor and pre ^ point.xor != 0:
            point, pre = get_pointer(pre ^ point.xor), point
        newnode = ListNode(element)
        point.xor = pre ^ dereference_pointer(newnode)
        return

    def get(self, index):
        pre = self.head
        point = dereference_pointer(self.head.xor)
        start = 0

        while start < index and pre ^ point.xor != 0:
            point, pre = get_pointer(pre ^ point.xor), point
            start += 1
        if pre ^ point.xor == 0:
            return None
        else:
            return get_pointer(point).val

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

