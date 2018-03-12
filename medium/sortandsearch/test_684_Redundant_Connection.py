"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
"""
import collections

class Solution(object):
    def findRedundantConnection1(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        mp = collections.defaultdict(list)

        def dfs(src, dest):
            if src not in seen:
                seen.append(src)
                if src == dest:
                    return True
                return any(dfs(i, dest) for i in mp[src])

        for m, n in edges:
            seen = []
            if m in mp and n in mp and dfs(m, n):
                return (m, n)
            mp[n].append(m)
            mp[m].append(n)


    def findRedundantConnection2(self, edges):
        # here are many duplicate calculate in the method
        # method one will be much better
        mp = collections.defaultdict(list)
        for m, n in edges:
            mp[m].append(n)
            mp[n].append(m)

        def dfs(m, n):
            if m == n:
                return True
            if m not in seen:
                seen.append(m)
                return any(dfs(i, n) for i in mp[m] if not i in seen)


        for m, n in edges[::-1]:

            seen = [m]
            if any(dfs(i, n) for i in mp[m] if i != n):
                return (m, n)

    def findRedundantConnection_uninfind(self, edges):
        pass


if __name__ == '__main__':
    s = Solution()
    edges = [[1,2], [1,3], [2,3], [4, 5], [6, 7], [5, 2], [6, 1]]
    rt1 = s.findRedundantConnection1(edges)
    print rt1

    rt2 = s.findRedundantConnection2(edges)
    print rt2
