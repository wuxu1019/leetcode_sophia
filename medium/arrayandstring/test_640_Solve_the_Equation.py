"""
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"

"""


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        l, r = equation.split('=')
        lmp = self.changestr(l)
        rmp = self.changestr(r)
        x = lmp['x'] - rmp['x']
        n = rmp['n'] - lmp['n']
        if not x:
            if lmp['n'] == rmp['n']:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x={0}".format(n / x)

    def changestr(self, s):
        ct = {'x': 0, 'n': 0}
        i = 0
        sign = 1;
        digt = 0;
        end = False
        while i < len(s):
            if s[i] == '+' or s[i] == '-':
                ct['n'] += sign * digt
                end = False
                digt = 0
                sign = -1 if s[i] == '-' else 1
            elif s[i] == 'x':
                if end:
                    ct['x'] += sign * digt
                else:
                    ct['x'] += sign
                end = False
                digt = 0
            else:
                digt = digt * 10 + int(s[i])
                end = True
            i += 1
        ct['n'] += sign * digt
        return ct