"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator1(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.list = nestedList

    def next(self):
        """
        :rtype: int
        """

        def helper(l):
            for i in l:
                if i.isInteger():
                    l.remove(i)
                    return i.getInteger()
                if self.hasNextHelper(i.getList()):
                    return helper(i.getList())

        return helper(self.list)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.hasNextHelper(self.list)

    def hasNextHelper(self, l):
        if not l:
            return False
        if l[0].isInteger():
            return True
        return self.hasNextHelper(l[0].getList()) or self.hasNextHelper(l[1:])

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


class NestedIterator2(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.list.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.list:
            if self.list[-1].isInteger():
                return True
            p = self.list.pop().getList()[::-1]
            self.list.extend(p)
        return False
