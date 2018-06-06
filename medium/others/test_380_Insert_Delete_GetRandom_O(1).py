"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

"""


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.l = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            return False
        else:
            self.data[val] = 1
            self.l.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            del self.data[val]
            pos = self.l.index(val) # This is not O(1), index is O(n)
            self.l[-1], self.l[pos] = self.l[pos], self.l[-1]
            self.l.pop()
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.l)


class RandomizedSet:

    def __init__(self):
        # do intialization if necessary
        self.data = []
        self.pos = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):
        # write your code here
        if val in self.pos:
            return False
        self.pos[val] = len(self.data)
        self.data.append(val)

        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        # write your code here
        if val not in self.pos:
            return False
        last, p = self.data[-1], self.pos[val]
        self.pos[last] = p
        self.data[p] = last
        self.data.pop()
        del self.pos[last]
        return True

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        import random
        # write your code here
        if self.data:
            return self.data[random.choice(range(0, len(self.data)))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
