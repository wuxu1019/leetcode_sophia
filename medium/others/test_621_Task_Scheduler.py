"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

"""

import collections
import copy

class Solution(object):

    def leastInterval_basic(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        ct = 0
        mp = sorted(collections.Counter(tasks).values(), reverse=1)
        n += 1
        while mp:
            l = len(mp)
            if l > n:
                mp = [i - 1 for i in mp[:n] if i - 1 > 0] + mp[n:]
                mp.sort(reverse=1)
            else:
                mp = [i - 1 for i in mp if i - 1 > 0]
            if not mp:
                ct += l
            else:
                ct += n
        return ct

    def leastInterval_findroutine(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        ct = collections.Counter(tasks).values()
        M = max(ct)
        Mct = ct.count(M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)

if __name__ == '__main__':
    s = Solution()
    task = ["A","A","A","B","B","B"]
    n = 2
    rt1 = s.leastInterval_findroutine(task, n)
    print rt1

    task = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2

    rt2 = s.leastInterval_findroutine(task, n)
    print rt2