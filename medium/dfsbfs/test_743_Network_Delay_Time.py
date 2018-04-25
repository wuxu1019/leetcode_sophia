"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

"""


class Solution(object):
    def networkDelayTime_dfs(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        times_n = collections.defaultdict(list)
        for src, dest, time in times:
            times_n[src].append((dest, time))

        signal = [float('INF')] * (N + 1)
        signal[0] = signal[K] = 0
        self.dfs(signal, times_n, K, 0)
        return -1 if float('INF') in signal else max(signal)

    def dfs(self, signal, times_n, p, base):
        if base > signal[p]:
            return
        signal[p] = base
        for dest, time in times_n[p]:
            self.dfs(signal, times_n, dest, base + time)

    def networkDelayTime_Dijkstra(self, times, N, K):