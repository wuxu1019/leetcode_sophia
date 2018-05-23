"""
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and fights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.

"""


class Solution(object):
    def findCheapestPrice_dfs(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        mp = collections.defaultdict(list)
        for s, d, p in flights:
            mp[s].append((d, p))
        self.ans = float('INF')
        self.findCheapestPriceHelper(mp, src, dst, K, 0)
        return self.ans if self.ans != float('INF') else -1

    def findCheapestPriceHelper(self, mp, src, dst, k, cost):

        if src == dst:
            self.ans = min(self.ans, cost)
            return
        if k < 0:
            return
        if src not in mp or not mp[src]:
            return
        for i in range(len(mp[src])):
            d, m = mp[src].pop()
            self.findCheapestPriceHelper(mp, d, dst, k - 1, cost + m)
            mp[src] = [(d, m)] + mp[src]

    def findCheapestPrice_dp(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        record = [float('INF')] * n
        record[src] = 0
        for k in range(K + 1):
            record_n = record[:]
            for a, b, c in flights:
                record_n[b] = min(record_n[b], record[a] + c)
            record = record_n

        return record[dst] if record[dst] != float('INF') else -1

    def findCheapestPrice_shortest_path(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

