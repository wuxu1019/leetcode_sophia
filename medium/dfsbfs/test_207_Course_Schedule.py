"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True

    def canFinish_2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        ct = collections.defaultdict(list)
        for a, b in prerequisites:
            ct[b].append(a)
        self.visit = [0] * numCourses
        self.iscycle = False

        def dfs(ct, point):
            self.visit[point] = 1
            for n in ct[point]:
                if self.visit[n] == -1:
                    continue
                elif self.visit[n] == 1:
                    self.iscycle = True
                    break
                else:
                    dfs(ct, n)
            self.visit[point] = -1

        for i in range(numCourses):
            if self.visit[i] == -1:
                continue
            dfs(ct, i)
            if self.iscycle:
                return False
        return True

    def canFinish_2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        ind = [[] for _ in xrange(numCourses)]  # indegree
        oud = [0] * numCourses  # outdegree
        for p in prerequisites:
            oud[p[0]] += 1
            ind[p[1]].append(p[0])
        dq = deque()
        for i in xrange(numCourses):
            if oud[i] == 0:
                dq.append(i)
        k = 0
        while dq:
            x = dq.popleft()
            k += 1
            for i in ind[x]:
                oud[i] -= 1
                if oud[i] == 0:
                    dq.append(i)
        return k == numCourses
