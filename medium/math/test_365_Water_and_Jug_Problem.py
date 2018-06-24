"""
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False

"""

class Solution(object):
    def canMeasureWater_bfs(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > x+ y:
            return False

        stk = [(0, 0)]
        visited = set([(0, 0)])

        while stk:
            a, b = stk.pop()
            if a + b == z:
                return True
            status = set()
            status.add((x, b))
            status.add((a, y))
            status.add((0, b))
            status.add((a, 0))
            status.add((min(x, a + b), 0 if a + b < x else a + b - x))
            status.add((0 if a < y - b else a - (y - b), min(y, a + b)))

            for i in status:
                if i not in visited:
                    visited.add(i)
                    stk.append(i)
        return False

    def canMeasureWater_math(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        import fractions
        if z > x + y:
            return False
        if z == 0:
            return True
        return z % fractions.gcd(x, y) == 0


