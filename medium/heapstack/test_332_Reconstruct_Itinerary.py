"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.


"""


class Solution(object):
    def findItinerary_dfs(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        mp = collections.defaultdict(list)
        for s, e in tickets:
            mp[s].append(e)
        for k in mp.keys():
            mp[k].sort()
        self.ans = None
        self.findItineraryHelper(mp, 'JFK', ['JFK'])
        return self.ans

    def findItineraryHelper(self, mp, start, base):
        if all(v == [] for v in mp.values()):
            self.ans = base
            return True
        if start in mp and mp[start]:
            dest = mp[start][:]
            for d in dest:
                mp[start].remove(d)
                if self.findItineraryHelper(mp, d, base + [d]):
                    return True
                mp[start].append(d)

        return False

    def findItinerary_stk(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        mp = collections.defaultdict(list)
        for s, e in tickets:
            mp[s].append(e)
        stack = ['JFK']
        result = []
        while len(stack) != 0:
            u = stack[-1]
            adj = mp[u]
            adj.sort(reverse=1)
            if len(adj) == 0:
                result.append(stack.pop())
            else:
                stack.append(adj.pop())
        result.reverse()
        return result