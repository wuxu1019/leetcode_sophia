"""
Description
Given a list of Connections, which is the Connection class (the city name at both ends of the edge and a cost between them), find some edges, connect all the cities and spend the least amount.
Return the connects if can connect all the cities, otherwise return empty list.

Return the connections sorted by the cost, or sorted city1 name if their cost is same, or sorted city2 if their city1 name is also same.

Have you met this question in a real interview?
Example
Gievn the connections = ["Acity","Bcity",1], ["Acity","Ccity",2], ["Bcity","Ccity",3]

Return ["Acity","Bcity",1], ["Acity","Ccity",2]
"""
import collections

class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost

class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        relation = collections.defaultdict(list)
        for i in connections:
            a, b = i.city1, i.city2
            relation[a].append((b, i))
            relation[b].append((a, i))
        city = len(relation.keys())
        self.mincost = float('INF')


        def dfs(root, base, route, cost):
            if len(base) == city:
                if cost < self.mincost:
                    self.mincost = cost
                    self.rt = route
                return

            for nex, rt in relation[root]:
                if nex not in base:
                    dfs(nex, base | set([nex]), route + [rt], cost + rt.cost)

        self.rt = []
        for start in relation.keys():
            dfs(start, set([start]), [], 0)
        print self.mincost
        return self.rt

if __name__ == '__main__':
    s = Solution()
    rt = s.lowestCost(
        [Connection("Acity","Bcity",1),
         Connection("Bcity","Ccity",3),
         Connection("Acity", "Ccity", 2)],
    )


    print(rt)



