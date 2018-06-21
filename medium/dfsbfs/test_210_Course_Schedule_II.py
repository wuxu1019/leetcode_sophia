"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        ct = collections.defaultdict(list)
        for a, b in prerequisites:
            ct[a].append(b)
        self.visited = [0] * numCourses
        self.ans = []
        self.hascycle = False

        def dfs(ct, i):
            self.visited[i] = 1
            for n in ct[i]:
                if self.visited[n] == -1:
                    continue
                elif self.visited[n] == 1:
                    self.hascycle = True
                    break
                else:
                    dfs(ct, n)
            self.visited[i] = -1
            self.ans.append(i)

        for i in range(numCourses):
            if self.visited[i] == -1:
                continue
            dfs(ct, i)
            if self.hascycle:
                return []
        return self.ans

        def findOrder_bfs(self, numCourses, prerequisites):
            """
            :type numCourses: int
            :type prerequisites: List[List[int]]
            :rtype: List[int]
            """

            outd = [0] * numCourses
            ind = collections.defaultdict(set)

            for a, b in prerequisites:
                outd[a] += 1
                ind[b].add(a)
            ans = []
            ct = 0
            q = collections.deque([n for n, v in enumerate(outd) if v == 0])

            while q:
                x = q.popleft()
                ans.append(x)
                ct += 1
                for i in ind[x]:
                    outd[i] -= 1
                    if outd[i] == 0:
                        q.append(i)
            return ans if ct == numCourses else []

        def findOrder_dfs(self, numCourses, prerequisites):
            """
            :type numCourses: int
            :type prerequisites: List[List[int]]
            :rtype: List[int]
            """

            outd = [0] * numCourses
            ind = collections.defaultdict(set)

            for a, b in prerequisites:
                outd[a] += 1
                ind[b].add(a)
            ans = []
            ct = 0
            stk = [n for n, v in enumerate(outd) if v == 0]

            while stk:
                x = stk.pop()
                ans.append(x)
                ct += 1
                for i in ind[x]:
                    outd[i] -= 1
                    if outd[i] == 0:
                        stk.append(i)
            return ans if ct == numCourses else []
