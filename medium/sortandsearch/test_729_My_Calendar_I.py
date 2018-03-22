"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""


class MyCalendar1(object):

    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        pos = 0
        for interval in self.intervals:
            if end <= interval[0]:
                continue
            elif start >= interval[1]:
                pos += 1
            else:
                return False
        self.intervals.insert(pos, (start, end))
        return True


class node(object):

    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None


class MyCalendar2(object):

    def __init__(self):
        self.root = None

    def bookHelper(self, root, s, e):
        if s >= root.e:
            if root.right:
                return self.bookHelper(root.right, s, e)
            else:
                root.right = node(s, e)
                return True
        elif e <= root.s:
            if root.left:
                return self.bookHelper(root.left, s, e)
            else:
                root.left = node(s, e)
                return True
        return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = node(start, end)
            return True
        return self.bookHelper(self.root, start, end)